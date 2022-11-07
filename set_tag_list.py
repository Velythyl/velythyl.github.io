#!/bin/python3
# This is meant to be used as a pre-commit hook

import os
tags = []
for post in os.listdir("./_posts"):
    with open(f"./_posts/{post}") as f:
        tags += f.read().split("tags: ")[1].split("\n")[0].split(" ")

tags = list(set(tags))
print(tags)

with open("_config.yml", 'r') as yml:
    beg, end = yml.read().split("display_tags")
    end = "\n".join(end.split("\n")[1:])
    file = f"{beg}display_tags: {str(tags)}\n{end}"

for x in range(20): # absolute jank but who cares
    file.replace("\n\n", "\n")

with open("_config.yml", 'w') as yml:
    yml.write(file)

import subprocess
subprocess.check_output("git add _config.yml", shell=True, universal_newlines=True)