#!/bin/python3
import os
tags = []
for post in os.listdir("./_posts"):
    with open(f"./_posts/{post}") as f:
        tags += f.read().split("tags: ")[1].split("\n")[0].split(" ")

tags = list(set(tags))
print(tags)

import yaml

with open("_config.yml", 'r') as stream:
    try:
        loaded = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# Modify the fields from the dict
loaded['display_tags'] = str(tags)

# Save it again
with open("_config.yml", 'w') as stream:
    try:
        yaml.dump(loaded, stream, default_flow_style=False)
    except yaml.YAMLError as exc:
        print(exc)