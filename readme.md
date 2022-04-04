
# amanahuja's website

Website published at: [amanahuja.me](https://amanahuja.me)

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

## Doing stuff

**Build quartz files before publishing.**

There's a helper script in this repo called `makequartz.sh`. The key idea is: 
```
hugo-obsidian -input=content -output=static -index -root=.
```


**To publicly publish a draft with ngrok**

Ngrok exposes local servers behind NATs and firewalls to the public internet over secure tunnels. See [docs](ngrok.com/docs). 
```
# start ngrok
$ ngrok http 1313

# get id from stdout
# e.g. https://7fb1-24-15-121-5.ngrok.io

# serve hugo on the IP
hugo serve -D --debug -b https://7fb1-24-15-121-5.ngrok.io --appendPort=false
```

