#!/usr/bin/env python3

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as f1:
  f1_contents = f1.read()

with open(file2) as f2:
  f2_contents = f2.read()

with open(file1, "w") as f1:
  f1.write(f2_contents)

with open(file2, "w") as f2:
  f2.write(f1_contents)
