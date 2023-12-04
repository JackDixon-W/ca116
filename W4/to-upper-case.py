#!/usr/bin/env python3

n = input()
i = 0
ans = ""

while i < len(n):
  if n[i] >= "a" and n[i] <= "z":
    ans += chr(ord(n[i]) - 32)
  else:
    ans += n[i]
  i += 1

print(ans)
