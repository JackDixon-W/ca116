#!/usr/bin/env python3

with open("characters.txt") as f:
  inp = f.read()

i = 0
while i < len(inp):
  if inp[i] != "\n":
    print(inp[i])
  else:
    print("")
  i += 1
