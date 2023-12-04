#!/usr/bin/env python3

i = 0
n = input()
ans = ""

while i < len(n):
  if n[i] != " ":
    ans += n[i]
  i += 1

print(ans)
