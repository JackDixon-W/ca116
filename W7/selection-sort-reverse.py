#!/usr/bin/env python3

i = 0
n = input()
nums = []

while n != "end":
  nums.append(int(n))
  high = int(n)
  n = input()

pos = 0
while i < len(nums):
  p = i
  pos = p
  high = nums[i]
  while p < len(nums):
    if high < nums[p]:
      high = nums[p]
      pos = p
    p += 1
  temp = nums[i]
  nums[i] = nums[pos]
  nums[pos] = temp
  i += 1

i = 0
while i < len(nums):
  print(nums[i])
  i += 1
