#!/usr/bin/env python3

import sys

csv = sys.argv[1]
i = 0
j = 0
data = []

while csv[i] != "=":
  i += 1

field = csv[:i]
value = csv[i + 1:]
i = 0

n = input()
while n != "end":
  data.append(n)
  n = input()

pos = 0
while data[0][i:i + len(field)] != field:
  while data[0][j] != ",":
    j += 1
  j += 1
  pos += 1
  i = j

i = 0
while i < len(data):
  j = 0
  pnt = 0
  while j < len(data[i]) and pnt < pos:
    j += 1
    if data[i][j] == ",":
      pnt += 1
  if j != 0:
    j += 1
  if data[i][j:j + len(value)] == value:
    print(data[i])
  i += 1
