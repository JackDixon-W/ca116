#!/usr/bin/env python3

import sys

lines = sys.stdin.read().split("\n")
lines = lines[:len(lines) - 1]

i = 0
output = ""
while i < len(lines):
  cur = lines[i].split()
  file = "page-" + cur[0] + ".txt"
  with open(file) as f:
    line = f.readlines()
    line = line[int(cur[1])]
  output += line[int(cur[2])]
  i += 1

print(output.rstrip("\n"))
