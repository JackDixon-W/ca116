#!/usr/bin/env python3

n = input()
i = 0
data = []

while n != "end":
  data.append(n)
  n = input()

while i < len(data):
  cur = data[i].split()
  cur[2] = int(cur[2])
  if cur[2] >= 2:
    print(data[i])
  i += 1
