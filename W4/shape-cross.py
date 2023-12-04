#!/usr/bin/env python3

i = 0
n = int(input())

while i < n:
  if i == (n // 2):
    print("*" * n)
  else:
    print(" " * (n // 2) + "*")
  i += 1
