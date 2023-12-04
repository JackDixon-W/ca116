#!/usr/bin/env python3

i = 0
n = input()
a = []

while n != "end":
  a.append(n)
  n = input()

while i < len(a):
  print(i, len(a), a[i])
  i += 1
