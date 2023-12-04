#!/usr/bin/env python3

import sys
import re

n = input()
i = 0
lines = []

while n != "end":
  lines.append(n)
  n = input()

while i < len(lines):
  if re.search(sys.argv[1], lines[i]):
    print(lines[i])
  i += 1
