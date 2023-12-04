#!/usr/bin/env python3

i = 0
lines = []
n = input()

while n != "end":
  lines.append(n)
  n = input()

while i < len(lines):
  print(lines[len(lines) - i - 1])
  i += 1
