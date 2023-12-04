#!/usr/bin/env python3

import sys

words = sys.stdin.read().split("\n")
words = words[:len(words) - 1]
seen = {}

j = 0
while j < len(words):
  seen[words[j]] = False
  j += 1

i = 0
while i < len(words):
  if seen[words[i]] is True:
    print("snap: " + words[i])
    i += len(words)
  else:
    seen[words[i]] = True
  i += 1
