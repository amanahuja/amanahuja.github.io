# Aman website common commands

set shell := ["bash", "-cu"]

# List all available recipes (default)
_default:
    @just --list

# Create a new post and open in nvim. Usage: just newpost my-post-title
newpost title:
    hugo new posts/{{title}}.md
    nvim content/posts/{{title}}.md

# Create a new portfolio entry and open in nvim. Usage: just newportfolio my-entry-title
newportfolio title:
    hugo new portfolio/{{title}}.md
    nvim content/portfolio/{{title}}.md
