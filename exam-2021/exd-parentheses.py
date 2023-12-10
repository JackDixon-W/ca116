#!/usr/bin/env python3

import sys

lines = sys.stdin.read().split("\n")
i = 0

while i < len(lines) - 1:
  cur = lines[i]
  first = len(cur)
  second = len(cur)
  pos = 0
  while pos < len(cur):
    if cur[pos] == "(" and first == len(cur):
      first = pos + 1
    if cur[pos] == ")" and second == len(cur):
      second = pos
    pos += 1
  if first != len(cur):
    print(cur[first:second])
  i += 1
