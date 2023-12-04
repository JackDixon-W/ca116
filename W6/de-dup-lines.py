#!/usr/bin/env python3

dup = []
n = input()

while n != "end":
  i = 0
  while i < len(dup) and dup[i] != n:
    i += 1
  if i == len(dup):
    print(n)
    dup.append(n)
  n = input()
