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
  - Creates content/posts/<slug>/index.md (Hugo page bundle)
  - Converts HTML body to Markdown via markdownify
  - Prepends editorial note
  - Merges WP tags + categories into unified tags list
  - Downloads WordPress-hosted images into the bundle directory
  - Leaves external (non-WP) images as-is

Run with:
    uv run pafnuty-migrate/migrate.py
"""

import xml.etree.ElementTree as ET
import re
import os
import sys
import urllib.request
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
    heading_style=markdownify.ATX,     # ## style headings
    bullets="-",
    code_language_callback=None,
    strip=["script", "style"],
)


def clean_html(html: str) -> str:
    """Remove WordPress widget noise from HTML before conversion."""
    for pattern in WP_NOISE_PATTERNS:
        html = pattern.sub("", html)
    return html.strip()


def html_to_markdown(html: str) -> str:
    """Convert HTML to Markdown, with light post-processing."""
    md = markdownify.markdownify(html, **MD_OPTIONS)
    # Collapse 3+ blank lines to 2
    md = re.sub(r'\n{3,}', '\n\n', md)
    # Strip trailing whitespace on each line
    md = "\n".join(line.rstrip() for line in md.splitlines())
    return md.strip()


def merge_tags(wp_tags: list[str], wp_cats: list[str]) -> list[str]:
    """Merge WP tags and categories into a single deduplicated lowercased list."""
    combined = set()
    for t in wp_tags + wp_cats:
        if t:
            combined.add(t.strip().lower())
    # Remove very generic WP meta-categories that add no value
    combined.discard("uncategorized")
    combined.discard("pafnuties")   # internal WP organisational tag
    return sorted(combined)


def slugify_filename(url: str) -> str:
    """Extract a safe filename from an image URL."""
    path = urllib.parse.urlparse(url).path
    name = os.path.basename(path)
    # Strip WP resize suffixes like -300x210 before extension
    name = re.sub(r'-\d+x\d+(\.[a-z]+)$', r'\1', name, flags=re.IGNORECASE)
    return name


def rewrite_image_urls(md: str, url_to_local: dict[str, str]) -> str:
    """Replace remote image URLs with local filenames in Markdown."""
    for remote_url, local_name in url_to_local.items():
        # Also handle the ?w=NNN variants WordPress appends
        base_url = remote_url.split("?")[0]
        md = md.replace(remote_url, local_name)
        md = md.replace(base_url, local_name)
    return md


def download_images(
    post_dir: Path,
    html: str,
    log_lines: list[str],
    slug: str,
) -> dict[str, str]:
    """
    Download all WordPress-hosted images referenced in the HTML.
    Returns a mapping of {original_url: local_filename}.
    External (non-WP) images are skipped.
    """
    url_to_local: dict[str, str] = {}

    img_urls = re.findall(
        r'https?://[^\s"\'<>]+\.(?:png|jpg|jpeg|gif|webp)(?:\?[^\s"\'<>]*)?',
        html,
        re.IGNORECASE,
    )

    for url in img_urls:
        base_url = url.split("?")[0]
        is_wp = "wordpress.com" in url or "wp.com" in url or "pafnuty.wordpress.com" in url
        if not is_wp:
            log_lines.append(f"SKIP (external)  {slug}  {url}")
            continue
        if base_url in url_to_local:
            # Already downloaded under its base URL
            continue

        filename = slugify_filename(base_url)
        dest = post_dir / filename

        if dest.exists():
            url_to_local[base_url] = filename
            url_to_local[url] = filename
            log_lines.append(f"EXISTS           {slug}  {filename}")
            continue

        try:
            headers = {"User-Agent": "Mozilla/5.0 (compatible; migration-script/1.0)"}
            resp = requests.get(url, headers=headers, timeout=15)
            resp.raise_for_status()
            dest.write_bytes(resp.content)
            url_to_local[base_url] = filename
            url_to_local[url] = filename
            log_lines.append(f"OK               {slug}  {filename}  ({len(resp.content)} bytes)")
        except Exception as exc:
            log_lines.append(f"FAIL             {slug}  {url}  {exc}")

    return url_to_local


def build_frontmatter(
    title: str,
    date: str,
    tags: list[str],
    original_url: str,
) -> str:
    """Render Hugo YAML frontmatter."""
    # Escape double-quotes in title
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
    month_year = dt.strftime("%B %Y")
    return (
        f"*Originally published on "
        f"[pafnuty.wordpress.com]({original_url}) "
        f"in {month_year}. "
        f"Reposted here as part of pulling old writing into one place.*\n\n---\n"
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
    created = 0
    skipped = 0

    for post in published:
        title = post.find("title").text or "(untitled)"
        # Decode HTML entities in title
        title = title.replace("&quot;", '"').replace("&#039;", "'").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        slug = post.find("wp:post_name", NS).text or ""
        raw_date = post.find("wp:post_date", NS).text or ""
        date_str = raw_date[:10]  # YYYY-MM-DD
        link = post.find("link").text or f"https://pafnuty.wordpress.com/"

        # Build original WP URL from date + slug
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            original_url = f"https://pafnuty.wordpress.com/{dt.year}/{dt.month:02d}/{dt.day:02d}/{slug}/"
        except ValueError:
            original_url = link

        # Tags and categories
        wp_tags = [c.text for c in post.findall('category[@domain="post_tag"]') if c.text]
        wp_cats = [c.text for c in post.findall('category[@domain="category"]') if c.text]
        tags = merge_tags(wp_tags, wp_cats)

        # HTML body (first content:encoded element)
        encoded_els = post.findall("{http://purl.org/rss/1.0/modules/content/}encoded")
        raw_html = encoded_els[0].text if encoded_els and encoded_els[0].text else ""

        # Post bundle directory
        post_dir = POSTS_DIR / slug
        index_path = post_dir / "index.md"

        if index_path.exists():
            print(f"  SKIP (exists)  {slug}")
            skipped += 1
            continue

        if not dry_run:
            post_dir.mkdir(parents=True, exist_ok=True)

        # Download WP-hosted images
        url_to_local: dict[str, str] = {}
        if not dry_run and raw_html:
            url_to_local = download_images(post_dir, raw_html, log_lines, slug)

        # Clean and convert HTML
        clean = clean_html(raw_html)
        # Rewrite image URLs to local filenames before conversion
        for remote, local in url_to_local.items():
            clean = clean.replace(remote, local)
        md_body = html_to_markdown(clean)

        # Assemble final content
        frontmatter = build_frontmatter(title, date_str, tags, original_url)
        editorial_note = build_editorial_note(original_url, date_str)
        full_content = f"{frontmatter}\n\n{editorial_note}\n{md_body}\n"

        if not dry_run:
            index_path.write_text(full_content, encoding="utf-8")

        print(f"  OK  {date_str}  {slug}")
        created += 1

    # Write image download log
    if not dry_run and log_lines:
        IMAGE_LOG.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
        print(f"\nImage log written to {IMAGE_LOG}")

    print(f"\nDone. Created: {created}  Skipped (already exists): {skipped}")


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("DRY RUN — no files will be written.")
    process_posts(dry_run=dry_run)
