#!/usr/bin/env python3

import sys
a = sys.stdin.read().split()

sum = 0
i = 0
while i < len(a):
  sum += int(a[i])
  i += 1

print(sum)
