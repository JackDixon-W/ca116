#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
  lines[i] = lines[i].strip("\n")
  cur = lines[i].split("/")
  print(cur[len(cur) - 1])
  i += 1
