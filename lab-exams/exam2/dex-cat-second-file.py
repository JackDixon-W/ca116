#!/usr/bin/env python3

import sys
file1 = sys.argv[1]

with open(file1) as first:
  file2 = first.read().rstrip()

with open(file2) as second:
  print(second.read().rstrip())
