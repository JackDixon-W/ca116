#!/usr/bin/env python3

n = input()
i = 0
nums = []

while n != "end":
  nums.append(int(n))
  n = input()

while i < len(nums):
  p = i
  low = nums[i]
  pos = i
  while p < len(nums):
    if low > nums[p]:
      low = nums[p]
      pos = p
    p += 1
  temp = nums[i]
  nums[i] = nums[pos]
  nums[pos] = temp
  i += 1

print(nums[len(nums) // 2])
