#!/usr/bin/env python3

n = input()
i = 0
nums = []

if n != "end":
  low = int(n)

while n != "end":
  nums.append(int(n))
  if len(nums) == 1:
    low = int(n)
    pos = i
  n = input()

while i < len(nums):
  if low > nums[i] and not low == nums[i]:
    low = nums[i]
    pos = i
  i += 1

print(pos)
