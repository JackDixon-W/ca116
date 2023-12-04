#!/usr/bin/env python3

i = 0
n = 7
gap = n - 2
left_gap = 1

while i < n:
  if i < n // 2:
    print(" " * i + "*" + " " * (gap - (2 * i))+ "*")
  elif i == n // 2:
    print(" " * i + "*")
  else:
    print(" " * ((n // 2) - left_gap))
  i += 1
