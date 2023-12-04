#!/usr/bin/env python3

import sys

nums = sys.stdin.read().split()
count = {}

i = 0
max = int(nums[i])
while i < len(nums):
  if max < int(nums[i]):
    max = int(nums[i])
  i += 1

i = 0
while i <= max:
  count[i] = 0
  i += 1

i = 0
while i < len(nums):
  count[int(nums[i])] += 1
  i += 1

h_freq = count[0]
for keys in count:
  if h_freq < count[keys]:
    h_freq = count[keys]

while y < h_freq:
  pos = 0
  while pos < max:
    if nums[pos] >= count[y]:
       
