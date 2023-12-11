#!/usr/bin/env python3

import sys
num = int(sys.argv[1])
num1 = 1
num2 = 1
total = 0
most_recent = 0

while num2 < num:
  if num1 % 2 == 0:
    total += num1
    most_recent = num1
  temp = num2
  num2 = num1 + num2
  num1 = temp

if num1 != most_recent and num1 % 2 == 0:
  total += num1

print(total)
