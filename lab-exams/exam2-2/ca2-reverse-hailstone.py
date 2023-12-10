#!/usr/bin/env python3

import sys
num = int(sys.argv[1])
hailstone = [num]

i = 0
while i < 9:
  if hailstone[i] % 2 == 0:
    hailstone.append(hailstone[i] // 2)
  else:
    hailstone.append(hailstone[i] * 3 + 1)
  i += 1

while i >= 0:
  print(hailstone[i])
  i -= 1
