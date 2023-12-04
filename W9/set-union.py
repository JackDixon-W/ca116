#!/usr/bin/env python3

words = {}
i = 0
with open("a.txt") as a:
  temp = a.read().split()
  while i < len(temp):
    words[temp[i]] = True
    i += 1

i = 0
with open("b.txt") as b:
  temp = b.read().split()
  while i < len(temp):
    words[temp[i]] = True
    i += 1

for key in words:
  print(key)
