#!/usr/bin/env python3

i = 0
odd = []
s = input()
n = 0

while s != "end":
  n = int(s)
  if n % 2 == 0:
    print(n)
  else:
    odd.append(n)
  s = input()

while i < len(odd):
  print(odd[i])
  i += 1
