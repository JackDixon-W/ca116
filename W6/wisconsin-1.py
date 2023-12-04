#!/usr/bin/env python3

n = input()

while n != "end":
  i = 0
  while i < len(n) and n[i] != ",":
    i += 1
  if n[i + 1:i + 3] == "WI":
    print(n[:i])
  n = input()
