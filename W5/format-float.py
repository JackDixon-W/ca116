#!/usr/bin/env python3

s = input()
i = 0
j = 0
left = ""
right = ""
prefix = ""

if s[i] == "-":
  prefix = "-"
  s = s[1:]

while i < len(s) and s[i] != ".":
  left += s[i]
  i += 1

if i == 0:
  left += "0"

if i + 1 >= len(s):
  right += "0"

while i + 1 < len(s):
  right += s[i + 1]
  i += 1

print(prefix + left + "." + right)
