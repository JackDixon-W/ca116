#!/usr/bin/env python3

i = 0
n = input()
data = []

while n != "end":
  data.append(n)
  n = input()

while i < len(data):
  out = data[i].split()
  print(" ".join(out[5:]))
  i += 1
