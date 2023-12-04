#!/usr/bin/env python3

i = 0
largest = int(input())

while i < 9:
  n = int(input())
  if n > largest:
    largest = n
  i += 1

print(largest)
