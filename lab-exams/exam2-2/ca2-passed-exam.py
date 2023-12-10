#!/usr/bin/env python3

import sys
names = sys.stdin.read().split("\n")
names = names[:len(names) - 1]

i = 0
while i < len(names):
  cur = names[i]
  if int(cur[len(cur) - 3:]) >= 40:
    print(cur[:len(cur) - 3])
  i += 1
