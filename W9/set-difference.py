#!/usr/bin/env python3

i = 0
seen = {}
with open("a.txt") as a:
  temp = a.read().split()
  read = 0
  while read < len(temp):
    seen[temp[read]] = True
    read += 1

with open("b.txt") as b:
  temp = b.read().split()
  read = 0
  while read < len(temp):
    seen[temp[read]] = False
    read += 1

for key in seen:
  if seen[key] is True:
    print(key)
