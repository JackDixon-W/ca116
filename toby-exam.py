#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
a = []

i = 0
while i < len(lines):
  x = len(lines[i]) - 3
  curr = lines[i][x:]
  a.append(curr)
  i += 1

num = []

j = 0
while j < len(a):
  number = int(a[j])
  num.append(number)
  j += 1

k = 0
total = 0
while k < len(num):
  total += num[k]
  k += 1

average = (total // len(num))

m = 0
while m < len(lines):
  y = int(lines[m][len(lines[m]) - 3:])
  if average < y:
    print(lines[m][:(len(lines[m]) - 3)])
  m += 1
