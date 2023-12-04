#!/usr/bin/env python3

n = int(input())
m = int(input())
i = 0

while i < n:
  if(m % 2 == 0):
    print(m)
    m = m // 2
  else:
    print(m)
    m = (m * 3) + 1
  i += 1
