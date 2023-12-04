#!/usr/bin/env python3

i = 0
lowest = int(input())

while i < 9:
  n = int(input())
  if n < lowest:
    lowest = n
  i += 1

print(lowest)
