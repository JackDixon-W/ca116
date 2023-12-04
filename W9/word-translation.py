#!/usr/bin/env python3

import sys

words = sys.stdin.read().split()

with open("translation.txt") as f:
  dict = {}
  doc = f.read().split("\n")
  doc = doc[:len(doc) - 1]
  j = 0
  while j < len(doc):
    line = doc[j].split()
    eng = line[0]
    ger = line[1]
    dict[eng] = ger
    j += 1
  i = 0
  while i < len(words):
    print(dict[words[i]])
    i += 1
