#!/usr/bin/env python3

n = int(input())
i = 0
last = 0
current = 1

while i + 1 < n:
  if(i == 0):
    print(last)
  print(current)
  storage = last
  last = current
  current = storage + current
  i += 1
