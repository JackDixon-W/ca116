#!/usr/bin/env python3

import sys
nums = sys.stdin.read().split()
dic = {}

i = 0
while i < 20:
  dic[i] = 0
  i += 1
i = 0

biggest = 0
while i < len(nums):
  dic[int(nums[i])] += 1
  if int(nums[i]) > biggest:
    biggest = int(nums[i])
  i += 1

i = biggest
while i > 0:
  j = 0
  output = " |"
  while j < 19:
    if dic[j] == i:
      output += "*"
    else:
      output += " "
    j += 1
  print(output)
  i -= 1

print(" -----------------------")

