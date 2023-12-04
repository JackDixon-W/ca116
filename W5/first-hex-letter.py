#!/usr/bin/env python3

n = int(input())
hex = str(hex(n))
i = 2

while i < len(hex) and not hex[i] >= "a" and hex[i] <= "z":
  i += 1

if i < len(hex):
  print(hex[i])
