
# amanahuja's website

Website published at: amanahuja.me

## Technical overview

Overview: 
* built using Hugo, hosted on Github Pages
* modified blogophonic theme
* ideas from the ananke theme, modified
* tachyons.io

Roadmap / tasks here on the [gh kanban](https://github.com/amanahuja/amanahuja.github.io/projects/1)
report issues here: https://github.com/amanahuja/amanahuja.github.io/issues

## Quartz

Leverages Jacky's Quartz for obsidian-like knowledge graph and backlinks. 
https://github.com/jackyzha0/quartz

Requires hugo-obsidian to build an index.
https://github.com/jackyzha0/hugo-obsidian

To serve locally:
```
hugo-obsidian -input=content -output=static -index -root=.
hugo server
```
