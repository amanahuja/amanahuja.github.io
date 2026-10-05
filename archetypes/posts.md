---
title: "{{ replace .Name "-" " " | title }}"
subtitle: "This shows up beneath the title on the post page"
# Provide `description` for intentional SEO and social-card copy. Without it,
# Hugo falls back to its automatic summary, normally the first 70 words.
description: ""
date: {{ .Date | dateFormat "2006-01-02" }}
author: "Aman Ahuja"
categories:
# Apply 1-3 per post. Available categories:
#   meta             — posts about this site or writing itself
#   reflections      — personal essays, observations, travel, culture
#   project-learnings — lessons from consulting/advisory engagements
#   reading-log      — reading notes and summaries
#   experiments      — technical explorations, algorithms, tinkering
#   observations     — commentary on things noticed in the world
  - 
tags:
# Use many. Have AI suggest tags based on draft content.
# will show up in fediverse bridged post header as "p-category"
# - origins
# - footag
series:
# For sequences with a defined order. Used rarely. Only one.
# - "LLM Evaluations" 
layout: single
draft: true
---

<!--
Using images: SOCIAL PREVIEW IMAGE (og:image): No image means no thumbnail when shared on
fediverse/social. To add one, use a page bundle (see below) and add the image
path to the `images` frontmatter field. Recommended dimensions: 1200x630px.
A site-wide fallback image (the logo) could be configured in head.html when ready.

If this post needs images, convert to a page bundle:

  content/posts/my-post/
    index.md      ← rename this file
    image.png

Then reference images as
`![alt](image.png)`

or with shortcode, this adds a caption, looks nice. 
`{{< figure src="image.jpg" alt="Alt text" caption="Caption" >}}`

Hack to control width, but losing caption
<img src="https://URL" style="width:150px" alt="alt text">

TABLES: needs a header row, a separator row (dashes, min 3 per column),
then data rows. The separator row is what makes Goldmark (Hugo's markdown
parser) recognize it as a table -- without it, pipes just render as plain
text. Theme styling (borders, zebra stripes, header caps) is automatic,
no extra markup needed.

| Header | Header |
| ------ | ------ |
| cell   | cell   |

Alignment is set per-column in the separator row (affects header + all
data cells in that column):
  :---   left (default)
  :---:  center
  ---:   right

| Left | Center | Right |
| :--- | :----: | ----: |
| a    |   b    |     c |
-->
