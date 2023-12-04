#!/usr/bin/env python3

import sys
files = sys.argv[1:]

i = 0
sum = 0
while i < len(files):
  with open(files[i]) as f:
    doc = f.read().strip("\n")
    doc = doc.split()
    j = 0
    while j < len(doc):
      if doc[j] != "\n" or doc[j] != " ":
        sum += int(doc[j])
      j += 1
  i += 1

print(sum)
