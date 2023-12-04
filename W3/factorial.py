#!/usr/bin/env python3

i = 0
factorial = 1
n = int(input())

while i < n:
  factorial *= (i + 1)
  i += 1

print(factorial)
