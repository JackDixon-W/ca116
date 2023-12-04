#!/usr/bin/env python3

i = 0
smallest = 10000

while i < 10:
  n = int(input())
  if(n < smallest and n > 0):
    smallest = n
  i += 1

print(smallest)
