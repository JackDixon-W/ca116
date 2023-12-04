#!/usr/bin/env python3

import sys

n = input()
i = 0

while n != "end":
  if sys.argv[1] in n:
    print(n)
  n = input()
