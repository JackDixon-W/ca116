#!/usr/bin/env python3

n = int(input())

final = ""
while n != 0:
  rem = n % 2
  n = n // 2
  final = str(rem) + final

print(final)
