#!/usr/bin/env python3

import sys
words = sys.stdin.read().split()

for element in words:
  if element[0] >= "A" and element[0] <= "Z":
    print(element)
