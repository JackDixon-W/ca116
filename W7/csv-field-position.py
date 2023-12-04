#!/usr/bin/env python3

import sys

n = input()
cv = sys.argv[1]
i = 0
j = 0
lcv = len(cv)
pos = 0

while n[i:i + lcv] != cv:
  while n[j] != ",":
    j += 1
  j += 1
  pos += 1
  i = j

print(pos)
