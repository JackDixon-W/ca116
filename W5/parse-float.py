#!/usr/bin/env python3

s = input()
i = 0
j = 0
left = ""
right = ""

while i < len(s) and s[i] != ".":
  left += s[i]
  i += 1

while i + 1 < len(s):
  right += s[i + 1]
  i += 1

print(left)
print(right)
