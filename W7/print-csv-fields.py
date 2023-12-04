#!/usr/bin/env python3

n = input()
csv = []

while n != "end":
  csv.append(n)
  n = input()

n = int(input())
i = 0
while i < len(csv):
  j = 0
  tally = 0
  while j < len(csv[i]) and tally < n:
    if csv[i][j] == ",":
      tally += 1
    j += 1
  k = j
  while k < len(csv[i]) and csv[i][k] != ",":
    k += 1
  print(csv[i][j:k])
  i += 1
