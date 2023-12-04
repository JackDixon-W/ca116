#!/usr/bin/env python3

import os
files = os.listdir(".")

with open("start.txt") as start:
  dest = start.read().rstrip()

# A new dictionary can be made without file types
# No . : With Dot
filesDic = {}
i = 0
while i < len(files):
  if "." in files[i]:
    pos = 0
    while pos < len(files[i]) and files[i][pos] != ".":
      pos += 1
    filesDic[files[i][:pos]] = files[i]
  i += 1

over = False
while over is False:
  if dest in filesDic:
    dest = filesDic[dest]
  if dest in files:
    with open(dest) as cur:
      dest = cur.read().rstrip()
  else:
    print(dest)
    over = True
