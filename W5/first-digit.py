#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and ("0" > s[i] or s[i] > "9"):
  i += 1

if i < len(s):
  print(s[i], i)
