#!/usr/bin/env python3

import sys

files = sys.argv[1:]
i = 0

sum = 0
while i < len(files):
  with open(files[i]) as f:
    lines = f.readlines()
    j = 0
    while j < len(lines):
      sum += int(lines[j])
      j += 1
  i += 1

print(sum)
