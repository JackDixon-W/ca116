#!/usr/bin/env python3

import sys

args = sys.argv[1:]
i = 0
total = 0

while i < len(args):
  num_args = int(args[i])
  total += num_args
  i += 1

print(total)
