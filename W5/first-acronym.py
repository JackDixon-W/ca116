#!/usr/bin/env python3

i = 0
n = input()
j = 0

while i < len(n) and (n[i] < "A" or n[i] > "Z"):
  i += 1

if i == 1:
  i -= 1

if i < len(n):
  j = i
  while i < len(n) and (n[i] >= "A" and n[i] <= "Z"):
    i += 1

if j < len(n) and n[j] >= "A" and n[j] <= "Z":
  print(n[j:i], j)
