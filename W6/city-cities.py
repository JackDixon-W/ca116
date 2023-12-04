#!/usr/bin/env python3

n = input()
n = input()

while n != "end":
  i = 0
  while i < len(n) and n[i] != ",":
    i += 1
  if "City" in n[:i]:
    print(n[:i])
  n = input()
