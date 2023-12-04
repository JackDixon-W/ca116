#!/usr/bin/env python3

n = input()
tally = 0

while n != "end":
  i = 0
  while i < len(n) and n[i] != ",":
    i += 1
  if n[i + 1:i + 3] == "WI":
    tally += 1
  n = input()

print(tally)
