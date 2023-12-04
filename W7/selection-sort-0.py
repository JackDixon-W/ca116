#!/usr/bin/env python3

n = input()
i = 0
nums = []

while n != "end":
  nums.append(int(n))
  low = int(n)
  n = input()

while i + 1 < len(nums):
  if nums[i] < nums[i + 1] and nums[i] < low:
    low = nums[i]
  i += 1

print(low)
