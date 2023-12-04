#!/usr/bin/env python3

i = 0
j = 1
n = input()

while i < len(n) and n[i] == n[-j]:
  i += 1
  if j == len(n) - 1:
    j -= 1
  j += 1

if i >= len(n) - 1:
  print("palindrome")
