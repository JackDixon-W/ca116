#!/usr/bin/env python3

import sys

inp = sys.stdin.read()
punc = {".": True, ",": True, "?": True, "!": True}

i = 0
tally = 0
while i < len(inp):
  if inp[i] in punc:
    tally += 1
  i += 1

print(tally)
