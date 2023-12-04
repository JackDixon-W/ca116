#!/usr/bin/env python3

n = input()
i = len(n)
t = ""

while i > 0:
  t += n[i - 1]
  i -= 1

print(t)
