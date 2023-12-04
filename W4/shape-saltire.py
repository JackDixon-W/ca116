#!/usr/bin/env python3

n = int(input())
half = n // 2

i = 0
while i < n:
  j = half - i
  if j < 0:
    j = -j
  if j == 0:
    print(half * " " + "*")
  else:
    print((half - j) * " " + "*" + (2 * j - 1) * " " + "*")

  i += 1
