#!/usr/bin/env python3

i = 0
n_string = input()
length = len(n_string)
n = int(n_string)
test = true

if length % 2 != 0:
  print("no")
else:
  left_side = n // (10 ** (length // 2))
  right_side = n % (10 ** (length // 2))

while i < (length // 2):
  if(right_side // (10 ** i)) != (left_side % (10 ** (i + 1))):
    test = true
  else:
    test = false
    break
  i += 1

if test = true:
  print("yes")
else
  print("no")
