#!/usr/bin/env python3

total = 0

while total != 1000:
  n = input()
  i = 0
  while i < len(n) and n[i] != "+":
    i += 1
  num1 = int(n[:i])
  num2 = int(n[i + 1:])
  total = num1 + num2
  print(total)
