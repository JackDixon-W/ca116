#!/usr/bin/env python3

import sys
num = int(sys.argv[1])

i = 0
while i < num and (i * i) < num:
  print(i)
  i += 1
