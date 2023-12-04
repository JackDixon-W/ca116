#!/usr/bin/env python3

i = 0
j = 0

while i < 10:
  n = input()
  j = 0
  while n[j] != "+":
    j += 1
  left = int(n[0:j])
  right = int(n[j + 1:])
  x = left + right
  print(x)
  i += 1
