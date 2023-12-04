#!/usr/bin/env python3

n = input()
i = 0
j = 0

while i < len(n):
  while j < len(n) and n[j] != ",":
    j += 1
  print(n[i:j])
  j += 1
  i = j
