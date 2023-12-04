#!/usr/bin/env python3

import sys

words = sys.stdin.read().split()
log = {}

i = 0
while i < len(words):
  log[words[i]] = False
  i += 1

i = 0
while i < len(words):
  if log[words[i]] is False:
    log[words[i]] = True
  elif log[words[i]] is True:
    log[words[i]] = "N"
  i += 1

j = 0
while j < len(words):
  if log[words[j]] != "N":
    print(words[j])
  j += 1
