#!/usr/bin/env python3

i = 0
n = input()
total = 0

while i < len(n):
  total += int(n[i:i + 1])
  i += 1

print(total)
