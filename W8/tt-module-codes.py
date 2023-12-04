#!/usr/bin/env python3

i = 0
n = input()
data = []

while n != "end":
  data.append(n)
  n = input()

while i < len(data):
  output = data[i].split()
  print(output[3])
  i += 1
