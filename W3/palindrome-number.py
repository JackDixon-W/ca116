#!/usr/bin/env python3

i = 0
n_string = input()
length = len(n_string)
n = int(n_string)
temp = n
rev = 0

while i < length:
  rev = (rev * 10) + (n % 10)
  n = n // 10
  i += 1

if rev == temp:
  print("yes")
else:
  print("no")
