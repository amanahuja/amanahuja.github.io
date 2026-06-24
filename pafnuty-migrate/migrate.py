# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "markdownify>=0.13",
#   "requests>=2.31",
# ]
# ///
"""
Pafnuty WordPress -> Hugo migration script.

For each published post in the WXR export:
  - Creates content/posts/<slug>/index.md (bundle) if images were downloaded
  - Creates content/posts/<slug>.md (flat file) if no local images
  - Converts HTML body to Markdown via markdownify
  - Applies wpautop to restore paragraph breaks on bare-newline posts
  - Converts WordPress [caption] shortcodes to Hugo {{< figure >}} shortcodes
  - Strips cosmetic inline <span style="..."> tags
  - Downloads WordPress-hosted images at full resolution (no ?w= resize params)
  - Leaves external (non-WP) images as-is
  - Prepends editorial note
  - Merges WP tags + categories into unified tags list

Run with:
    uv run pafnuty-migrate/migrate.py
    uv run pafnuty-migrate/migrate.py --dry-run
"""

import xml.etree.ElementTree as ET
import re
import os
import sys
import urllib.parse
from pathlib import Path
from datetime import datetime

import markdownify
import requests

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).parent.parent
XML_PATH = Path(__file__).parent / "pafnutyblog.WordPress.2026-06-24.xml"
POSTS_DIR = REPO_ROOT / "content" / "posts"
IMAGE_LOG = Path(__file__).parent / "image-download.log"

# ---------------------------------------------------------------------------
# XML namespaces
# ---------------------------------------------------------------------------
NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}

# ---------------------------------------------------------------------------
# Block-level HTML tags — used by wpautop to avoid wrapping them in <p>
# ---------------------------------------------------------------------------
BLOCK_TAGS = re.compile(
    r'^\s*<(div|p|ul|ol|li|blockquote|h[1-6]|pre|table|thead|tbody|tr|td|th'
    r'|figure|figcaption|hr|br|img|iframe|video|audio|script|style)',
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# WordPress noise patterns to strip before conversion
# ---------------------------------------------------------------------------
WP_NOISE_PATTERNS = [
    # Share buttons block
    re.compile(r'<div[^>]*class="[^"]*sharedaddy[^"]*".*?</div>\s*', re.DOTALL | re.IGNORECASE),
    # "Like" / "Like Loading..." widgets
    re.compile(r'<div[^>]*class="[^"]*wpl-button[^"]*".*?</div>\s*', re.DOTALL | re.IGNORECASE),
    re.compile(r'Like Loading\.\.\.\s*', re.IGNORECASE),
    # Related posts widgets
    re.compile(r'<div[^>]*class="[^"]*jp-relatedposts[^"]*".*?</div>\s*', re.DOTALL | re.IGNORECASE),
    # "Share this:" labels
    re.compile(r'<h3[^>]*>Share\s*(this)?:?\s*</h3>\s*', re.IGNORECASE),
]

# ---------------------------------------------------------------------------
# markdownify converter options
# ---------------------------------------------------------------------------
MD_OPTIONS = dict(
    heading_style=markdownify.ATX,
    bullets="-",
    code_language_callback=None,
    strip=["script", "style"],
)


def wpautop(html: str) -> str:
    """
    Approximate WordPress's wpautop() filter.
    Converts double-newline separated text blocks into <p>...</p> elements.
    Only applied to posts that have no existing <p> tags.
    """
    if re.search(r'<p[\s>]', html, re.IGNORECASE):
        return html  # Already has <p> tags, leave alone

    # Normalise line endings
    html = html.replace('\r\n', '\n').replace('\r', '\n')

    # Split on double newlines
    blocks = re.split(r'\n\n+', html)
    result = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # Don't wrap block-level elements in <p>
        if BLOCK_TAGS.match(block) or block.startswith('[caption'):
            result.append(block)
        else:
            # Replace single newlines within the block with <br>
            block = block.replace('\n', '<br>\n')
            result.append(f'<p>{block}</p>')

    return '\n\n'.join(result)


def convert_captions(html: str, url_to_local: dict[str, str]) -> str:
    """
    Convert WordPress [caption] shortcodes to Hugo {{< figure >}} shortcodes.

    Handles three patterns:
    1. [caption ...]<a href="LINK"><img src="SRC" .../></a> CAPTION[/caption]
    2. [caption ...]<img src="SRC" .../> CAPTION[/caption]
    3. [caption ... caption="CAPTION_ATTR"]<img src="SRC" .../>[/caption]

    Image SRC is rewritten to local filename if downloaded.
    """

    def extract_attr(tag: str, attr: str) -> str:
        m = re.search(rf'{attr}=["\']([^"\']*)["\']', tag, re.IGNORECASE)
        return m.group(1) if m else ""

    def local_src(src: str) -> str:
        """Rewrite src to local filename if we downloaded it."""
        base = src.split("?")[0]
        return url_to_local.get(src, url_to_local.get(base, src))

    def replace_caption(m: re.Match) -> str:
        caption_tag = m.group(1)   # the [caption ...] opening tag content
        inner = m.group(2).strip() # everything between [caption] and [/caption]

        # Extract caption text from attribute, or from trailing text after img/a
        caption_attr = extract_attr(caption_tag, "caption")

        # Try to find a wrapping <a> link
        link_match = re.search(r'<a\s[^>]*href=["\']([^"\']*)["\'][^>]*>', inner, re.IGNORECASE)
        link = link_match.group(1) if link_match else ""

        # Find the <img> tag
        img_match = re.search(r'<img\s([^>]*)/?>', inner, re.IGNORECASE)
        if not img_match:
            return inner  # Couldn't parse, leave as-is

        img_attrs = img_match.group(1)
        src = extract_attr(img_attrs, "src")
        alt = extract_attr(img_attrs, "alt") or extract_attr(img_attrs, "title")

        # Caption text: prefer attribute, else trailing text after the img/a block
        if caption_attr:
            caption = caption_attr
        else:
            # Strip all HTML tags from inner and get remaining text
            no_tags = re.sub(r'<[^>]+>', '', inner).strip()
            caption = no_tags

        # Rewrite src to local if applicable
        src = local_src(src)

        # Build figure shortcode — escape double quotes inside parameter values
        def esc(s: str) -> str:
            return s.replace('"', '&quot;')

        parts = [f'src="{esc(src)}"']
        if alt:
            parts.append(f'alt="{esc(alt)}"')
        if caption:
            parts.append(f'caption="{esc(caption.strip())}"')
        if link:
            parts.append(f'link="{esc(link)}"')

        return '{{< figure ' + ' '.join(parts) + ' >}}'

    # Match [caption ...] ... [/caption] — non-greedy, dotall
    pattern = re.compile(
        r'\[caption([^\]]*)\](.*?)\[/caption\]',
        re.DOTALL | re.IGNORECASE,
    )
    return pattern.sub(replace_caption, html)


def strip_cosmetic_spans(html: str) -> str:
    """Strip <span style="..."> tags, keeping their inner content."""
    # Remove opening span tags with a style attribute
    html = re.sub(r'<span\s+style="[^"]*"[^>]*>', '', html, flags=re.IGNORECASE)
    # Remove closing </span> tags
    html = re.sub(r'</span>', '', html, flags=re.IGNORECASE)
    return html


def strip_wp_resize_params(url: str) -> str:
    """
    Return the full-resolution version of a WordPress image URL.
    Strips ?w=, ?h=, ?resize=, ?fit=, ?zoom= query params.
    Also strips WP dimension suffixes like -300x223 from the filename.
    """
    # Strip query string entirely
    base = url.split("?")[0]
    # Strip -WIDTHxHEIGHT suffix before extension, e.g. image-300x223.jpg -> image.jpg
    base = re.sub(r'-\d+x\d+(\.[a-zA-Z]+)$', r'\1', base)
    return base


def clean_html(html: str) -> str:
    """Remove WordPress widget noise and cosmetic spans from HTML."""
    for pattern in WP_NOISE_PATTERNS:
        html = pattern.sub("", html)
    html = strip_cosmetic_spans(html)
    return html.strip()


def html_to_markdown(html: str) -> str:
    """Convert HTML to Markdown, with light post-processing."""
    md = markdownify.markdownify(html, **MD_OPTIONS)
    # Collapse 3+ blank lines to 2
    md = re.sub(r'\n{3,}', '\n\n', md)
    # Strip trailing whitespace on each line
    md = "\n".join(line.rstrip() for line in md.splitlines())
    # Fix escaped underscores inside Hugo shortcode lines — markdownify
    # escapes underscores for Markdown emphasis, but shortcodes are not Markdown
    md = fix_shortcode_escaping(md)
    return md.strip()


def fix_shortcode_escaping(md: str) -> str:
    """
    markdownify escapes underscores (\_) inside Hugo shortcode lines.
    Unescape them — shortcode lines are passed through Hugo as-is, not parsed as Markdown.
    A shortcode line is any line containing Hugo shortcode delimiters.
    """
    lines = md.splitlines()
    result = []
    for line in lines:
        if '{{<' in line and '>}}' in line:
            line = line.replace('\\_', '_')
        result.append(line)
    return "\n".join(result)


def merge_tags(wp_tags: list[str], wp_cats: list[str]) -> list[str]:
    """Merge WP tags and categories into a single deduplicated lowercased list."""
    combined = set()
    for t in wp_tags + wp_cats:
        if t:
            combined.add(t.strip().lower())
    combined.discard("uncategorized")
    combined.discard("pafnuties")
    return sorted(combined)


def slugify_filename(url: str) -> str:
    """Extract a safe filename from a full-resolution image URL (no query params)."""
    path = urllib.parse.urlparse(url).path
    return os.path.basename(path)


def download_images(
    dest_dir: Path,
    html: str,
    log_lines: list[str],
    slug: str,
) -> dict[str, str]:
    """
    Download all WordPress-hosted images at full resolution.
    Returns a mapping of {original_url_variant: local_filename} covering
    both the original URL (with ?w= params) and the clean base URL.
    External (non-WP) images are skipped.
    """
    url_to_local: dict[str, str] = {}

    # Find all image URLs including those with query params
    raw_urls = re.findall(
        r'https?://[^\s"\'<>]+\.(?:png|jpg|jpeg|gif|webp)(?:\?[^\s"\'<>]*)?',
        html,
        re.IGNORECASE,
    )

    seen_full_res: set[str] = set()

    for raw_url in raw_urls:
        is_wp = (
            "wordpress.com" in raw_url
            or "wp.com" in raw_url
            or "pafnuty.files.wordpress.com" in raw_url
        )
        if not is_wp:
            log_lines.append(f"SKIP (external)  {slug}  {raw_url}")
            continue

        full_res_url = strip_wp_resize_params(raw_url)

        if full_res_url in seen_full_res:
            # Already processed this image; just add the raw variant mapping
            if full_res_url in url_to_local:
                url_to_local[raw_url] = url_to_local[full_res_url]
            continue
        seen_full_res.add(full_res_url)

        filename = slugify_filename(full_res_url)
        dest = dest_dir / filename

        if dest.exists():
            url_to_local[full_res_url] = filename
            url_to_local[raw_url] = filename
            log_lines.append(f"EXISTS           {slug}  {filename}")
            continue

        try:
            headers = {"User-Agent": "Mozilla/5.0 (compatible; migration-script/1.0)"}
            resp = requests.get(full_res_url, headers=headers, timeout=15)
            resp.raise_for_status()
            dest.write_bytes(resp.content)
            url_to_local[full_res_url] = filename
            url_to_local[raw_url] = filename
            log_lines.append(f"OK               {slug}  {filename}  ({len(resp.content)} bytes)")
        except Exception as exc:
            log_lines.append(f"FAIL             {slug}  {full_res_url}  {exc}")

    return url_to_local


def build_frontmatter(title: str, date: str, tags: list[str]) -> str:
    """Render Hugo YAML frontmatter."""
    safe_title = title.replace('"', '\\"')
    tags_yaml = "\n".join(f'  - {t}' for t in tags) if tags else ""
    fm = f"""---
title: "{safe_title}"
date: {date}
author: "Aman Ahuja"
series:
  - pafnuty-blog
"""
    if tags_yaml:
        fm += f"tags:\n{tags_yaml}\n"
    fm += """categories:
  - CHANGETHISCATEGORY
layout: single
draft: false
---"""
    return fm


def build_editorial_note(original_url: str, date_str: str) -> str:
    """Build the repost editorial note."""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    date_display = dt.strftime("%B %d, %Y").replace(" 0", " ")  # e.g. "November 27, 2012"
    consolidation_url = "/posts/consolidating-my-writing/"
    return (
        f"*Originally published on my old blog, "
        f"[Pafnuty blog]({original_url}). "
        f"Reposted here as an effort to "
        f"[consolidate writing]({consolidation_url}) into one place. "
        f"The original publication date was: {date_display}.*\n\n---\n"
    )


def process_posts(dry_run: bool = False) -> None:
    print(f"Parsing {XML_PATH} ...")
    tree = ET.parse(XML_PATH)
    root = tree.getroot()

    items = root.findall(".//item")
    published = [
        i for i in items
        if (
            i.find("wp:post_type", NS) is not None
            and i.find("wp:post_type", NS).text == "post"
            and i.find("wp:status", NS) is not None
            and i.find("wp:status", NS).text == "publish"
        )
    ]
    published.sort(key=lambda p: p.find("wp:post_date", NS).text)

    print(f"Found {len(published)} published posts.")
    log_lines: list[str] = []
    created_bundle = 0
    created_flat = 0
    skipped = 0

    for post in published:
        title = post.find("title").text or "(untitled)"
        title = (title
                 .replace("&quot;", '"')
                 .replace("&#039;", "'")
                 .replace("&amp;", "&")
                 .replace("&lt;", "<")
                 .replace("&gt;", ">"))
        slug = post.find("wp:post_name", NS).text or ""
        raw_date = post.find("wp:post_date", NS).text or ""
        date_str = raw_date[:10]
        link = post.find("link").text or "https://pafnuty.wordpress.com/"

        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            original_url = f"https://pafnuty.wordpress.com/{dt.year}/{dt.month:02d}/{dt.day:02d}/{slug}/"
        except ValueError:
            original_url = link

        wp_tags = [c.text for c in post.findall('category[@domain="post_tag"]') if c.text]
        wp_cats = [c.text for c in post.findall('category[@domain="category"]') if c.text]
        tags = merge_tags(wp_tags, wp_cats)

        encoded_els = post.findall("{http://purl.org/rss/1.0/modules/content/}encoded")
        raw_html = encoded_els[0].text if encoded_els and encoded_els[0].text else ""

        # Check if either output path already exists — skip if so
        bundle_path = POSTS_DIR / slug / "index.md"
        flat_path = POSTS_DIR / f"{slug}.md"
        if bundle_path.exists() or flat_path.exists():
            print(f"  SKIP (exists)  {slug}")
            skipped += 1
            continue

        # --- Phase 1: download images (to a temp dir first so we know the count) ---
        url_to_local: dict[str, str] = {}
        if not dry_run and raw_html:
            # We need a real dir to download into; use bundle dir speculatively
            tmp_dir = POSTS_DIR / slug
            tmp_dir.mkdir(parents=True, exist_ok=True)
            url_to_local = download_images(tmp_dir, raw_html, log_lines, slug)
            # If no images were actually downloaded, remove the dir
            if not url_to_local:
                tmp_dir.rmdir()

        has_images = bool(url_to_local)

        # --- Phase 2: clean and convert HTML ---
        clean = clean_html(raw_html)
        clean = wpautop(clean)
        clean = convert_captions(clean, url_to_local)
        # Rewrite remaining image URLs (outside captions) to local filenames
        for remote, local in url_to_local.items():
            clean = clean.replace(remote, local)
        md_body = html_to_markdown(clean)

        # --- Phase 3: assemble content ---
        frontmatter = build_frontmatter(title, date_str, tags)
        editorial_note = build_editorial_note(original_url, date_str)
        full_content = f"{frontmatter}\n\n{editorial_note}\n{md_body}\n"

        # --- Phase 4: write to bundle or flat file ---
        if not dry_run:
            if has_images:
                out_path = POSTS_DIR / slug / "index.md"
                out_path.write_text(full_content, encoding="utf-8")
                created_bundle += 1
                print(f"  BUNDLE  {date_str}  {slug}")
            else:
                out_path = POSTS_DIR / f"{slug}.md"
                out_path.write_text(full_content, encoding="utf-8")
                created_flat += 1
                print(f"  FLAT    {date_str}  {slug}")
        else:
            # Dry run: just report what would happen
            layout = "BUNDLE" if has_images else "FLAT  "
            print(f"  {layout}  {date_str}  {slug}")
            if has_images:
                created_bundle += 1
            else:
                created_flat += 1

    if not dry_run and log_lines:
        IMAGE_LOG.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
        print(f"\nImage log written to {IMAGE_LOG}")

    print(f"\nDone. Bundles: {created_bundle}  Flat: {created_flat}  Skipped: {skipped}")


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("DRY RUN — no files will be written.")
    process_posts(dry_run=dry_run)
