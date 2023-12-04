#!/usr/bin/env python3

import sys

files = sys.argv
with open(files[1]) as a:
  alines = a.read().split("\n")

with open(files[2]) as b:
  blines = b.read().split("\n")

alines = alines[:len(alines) - 1]
blines = blines[:len(blines) - 1]

line = 0
pos = 0

if len(alines) < len(blines):
  line = len(alines)
  print(line, pos)
elif len(blines) < len(alines):
  line = len(blines)
  print(line, pos)
elif len(alines[len(alines) - 1]) < len(blines[len(blines) - 1]):
  line = len(alines)
  pos = len(alines[len(alines) - 1])
  print(line, pos)
elif len(blines[len(blines) - 1]) < len(alines[len(alines) - 1]):
  line = len(blines)
  pos = len(blines[len(blines) - 1])
  print(line, pos)
else:
  while line < len(alines):
    while pos < len(alines[line]):
      if alines[line][pos] != blines[line][pos]:
        print(line, pos)
        pos += len(alines[line])
      pos += 1
    line += 1
    pos = 0
