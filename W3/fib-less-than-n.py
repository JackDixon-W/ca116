#!/usr/bin/env python3

n = int(input())
i = 0
prev = 0
current = 1
temp = 0

print(prev)

while current < n:
  print(current)
  temp = prev
  prev = current
  current = current + temp
