#!/usr/bin/env python3

n = input()
i = 0
data = []
outputs = []

while n != "end":
  data.append(n)
  n = input()

while i < len(data):
  j = 0
  while j < len(data[i]) and data[i][j] != ",":
    j += 1
  if data[i][j + 1:j + 3] == "WI":
    outputs.append(data[i][:j])
  i += 1

k = 0
while k < len(outputs):
  print(outputs[k])
  k += 1
