# Aman website common commands

set shell := ["bash", "-cu"]

# List all available recipes (default)
_default:
    @just --list

# Create a new post and open in nvim. Usage: just newpost my-post-title
newpost title:
    hugo new posts/{{title}}.md
    nvim content/posts/{{title}}.md
