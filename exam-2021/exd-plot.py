#!/usr/bin/env python3

import sys
nums = sys.stdin.read().split()
length = int(nums[0])
nums = nums[1:]

i = 0
output = "|"
while i < length:
  if str(i) in nums:
    output += "*"
  else:
    output += " "
  i += 1
output += "|"

print(output)
