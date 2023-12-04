#!/usr/bin/env python3

import sys

locX = []
locY = []
locs = {}
inp = sys.stdin.read().split("\n")
inp = inp[:len(inp) - 1]

i = 0
j = 0
while j < len(inp):
  i = 0
  while inp[j][i] != " ":
    i += 1
  locX.append(inp[j][:i])
  locY.append(inp[j][i + 1:])
  temp = inp[j][:i] + "-" + inp[j][i + 1:]
  locs[temp] = True
  j += 1

print(" --------------------")

i = 19
while i >= 0:
  cur = "|"
  j = 0
  while j < 20:
    temp = str(j) + "-" + str(i)
    if temp in locs:
      cur += "*"
    else:
      cur += " "
    j += 1
  cur += "|"
  print(cur)
  i -= 1

print(" --------------------")
