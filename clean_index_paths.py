""""
This is a simple python script that modifies output created by 
hugo-obsidian to meet needs of this hugo theme. 

Specifically: 
    linkIndex is modified to update paths
        Step 1: Update linkIndex:index.links
        Step 2: Update linkIndex:index.backlinks
        Step 3: Update linkIndex:links
    contentIndex is modified to update paths
        Step 4: Update contentIndex

These are confusing names, and I'm not entirely sure what they do. 
I'm replicating functionality by hugo-obsidian. For more information 
please see
    https://github.com/jackyzha0/hugo-obsidian/

Reuse of this script is not recommended. 

author: @amanahuja
https://github.com/amanahuja/amanahuja.github.io

"""
import os
import json

### Set option
datadir = 'static'
quartz_content_dir = 'content/garden/' # this is currently hardcoded

"""
Helper Functions
"""

def add_prefix(s): 
    """Adds a path prefix 
    """
    if not s.startswith('/garden'): 
        return '/garden/' + s.lstrip('/')
    else: 
        return s

def smart_prefix(path):
    """Checks head of path, calls add_prefix or returns False"""
    ss = path.rstrip('/')
    
    head, tail = os.path.split(ss)
    if head == '/': 
        return add_prefix(tail)
    else:
        return False

print (f"Using datadir = {datadir}")
file_linkindex = os.path.join(datadir, "linkIndex.json")
file_contentindex = os.path.join(datadir, "contentIndex.json")

print ("Updating linkIndex.json")

with open(file_linkindex) as file: 
    data = json.load(file)

# Step 1: update data>index>links

data_index_links = data['index']['links']

new_dict = {} 
for link_key, link_list in data_index_links.items(): 
    
    # update data>index>links :: keys
    new_link_key = smart_prefix(link_key)
    if new_link_key: 
        new_dict[new_link_key] = link_list

# replace old dict with new dict
data['index']['links'] = new_dict


# Step 2: update data>index>backlinks

data_index_backlinks = data['index']['backlinks']

new_dict = {} 
for link_key, link_list in data_index_backlinks.items(): 
    
    # update data>index>backlinks :: keys
    new_link_key = smart_prefix(link_key)
    if new_link_key: 
        new_dict[new_link_key] = link_list

# replace old dict with new dict
data['index']['backlinks'] = new_dict

# Step 3: update data>links

data_links = data['links']

new_list = []
for link_data in data_links: 
    new_link_data = {}
    
    for v in ['source', 'target']:
        new_link_data[v] = smart_prefix(link_data[v])
    
    for v in ['text']: 
        new_link_data[v] = link_data[v]
    
    if all([new_link_data['source'], new_link_data['target']]): 
        new_list.append(new_link_data)

# replace old with new 
data['links'] = new_list

# Write data back to JSON file
with open(file_linkindex, 'w') as outfile: 
    json.dump(data, outfile, indent=2)

print ("Updating contentIndex.json")

with open(file_contentindex) as file: 
    data = json.load(file)

# update content index data

content_index = data
#print (content_index, "\n\n")

new_dict = {} 
for link_key, link_data in content_index.items(): 
    
    # update content index data :: keys
    new_link_key = smart_prefix(link_key)
    if new_link_key: 
        new_dict[new_link_key] = link_data

# replace old dict with new dict
data = new_dict

# Write data back to JSON file
with open(file_contentindex, 'w') as outfile: 
    json.dump(data, outfile, indent=2)


