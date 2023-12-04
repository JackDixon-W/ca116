#!/usr/bin/env python3

i = 0
storage = 0

while i < 10:
  n = int(input())
  storage += n * (10 ** i)
  i += 1

while i > 0:
  print((storage % (10 ** i)) // 10 ** (i - 1))
  i -= 1
