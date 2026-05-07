---
title: "{{ replace .Name "-" " " | title }}"
subtitle: "This shows up in previews (homepage and listing)"
date: {{ .Date | dateFormat "2006-01-02" }}
author: "Aman Ahuja"
categories:
# Apply 1-3 per post.
# Keep total to ~5. Add to archetype when new.
  - project-learnings
tags:
# Use many. Have AI suggest tags based on draft content.
# - origins
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

Then reference images as: ![alt](image.png)
-->
