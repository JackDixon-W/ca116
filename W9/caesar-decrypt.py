#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

crypt = {}

i = 0
while i < len(src):
  crypt[dst[i]] = src[i]
  i += 1

words = sys.stdin.read().strip("\n")

i = 0
out = ""
while i < len(words):
  if words[i] >= "a" and words[i] <= "z":
    out += crypt[words[i]]
  elif words[i] >= "A" and words[i] <= "Z":
    out += crypt[words[i]]
  else:
    out += words[i]
  i += 1

print(out)
