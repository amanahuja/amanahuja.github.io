
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

Uses `hugo-obsidian` to build an index.
* [hugo-obsidian](https://github.com/jackyzha0/hugo-obsidian) creates two JSON files as output: `static/linkIndex.json` and `static/contentIndex.json`. The script is available as a github action. See the quartz repo readme for details. 
* My own setup requires modifications to these indexes. These are scripted in python `clean_index_paths.py`. 
* Also consider: https://github.com/trojblue/Obsidian-wiki-fix to fix link styles for quarz, if needed. 

To serve locally:
```
hugo-obsidian -input=content -output=static -index -root=.
hugo server
```
