#!/usr/bin/env python3

n = input()
i = 0
data = []

while n != "end":
  data.append(n)
  n = input()

while i < len(data):
  if data[i][0] == "3":
    print(data[i])
  i += 1
