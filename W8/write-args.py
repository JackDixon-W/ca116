#!/usr/bin/env python3

import sys
file = sys.argv[1]
i = 2

with open(file, "w") as f:
  while i < len(sys.argv):
    cur = sys.argv[i] + "\n"
    f.write(cur)
    i += 1
