#!/usr/bin/env python3

offset = 0

nums = [0] * 999
s = input()
while s != "end":
    n = int(s)
    if nums[n + offset] == n:
        nums[n + offset + 1] = n
        offset += 1
    else:
        nums[n + offset] = n
    s = input()

i = 0
while i < len(nums):
    if nums[i] != 0 and i != 0:
        print(nums[i])
    i += 1
