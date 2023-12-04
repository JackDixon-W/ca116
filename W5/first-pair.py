#!/usr/bin/env python3

n = input()
i = 0
j = len(n)

while i < len(n) - 1:
  if n[i] == n[i + 1]:
    j = i
    i = len(n)
  i += 1

if j != len(n):
  print(n[j:j + 2])
