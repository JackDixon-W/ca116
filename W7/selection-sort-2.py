#!/usr/bin/env python3

n = input()
j = 0
nums = []

while n != "end":
  nums.append(int(n))
  n = input()

i = int(input())
j = nums[i]
pos = i
while i < len(nums):
  if j > nums[i]:
    pos = i
    j = nums[i]
  i += 1

print(pos)
