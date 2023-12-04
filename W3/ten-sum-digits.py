#!/usr/bin/env python3

i = 0
sum = 0

while i < 10:
  n = int(input())
  if n < 0:
    sum += (n * -1) % 10
  else:
    sum += n % 10
  i += 1

print(sum)
