#!/usr/bin/env python3

import sys

with open("boys.txt") as b:
  temp = b.read().strip("\n")
  namesB = temp.split()

with open("girls.txt") as g:
  temp = g.read().strip("\n")
  namesG = temp.split()

i = 0
boys = {}
while i < len(namesB):
  boys[namesB[i]] = True
  i += 1

j = 0
girls = {}
while j < len(namesG):
  girls[namesG[j]] = True
  j += 1

names = sys.stdin.read().split()
x = 0
while x < len(names):
  if names[x] in boys and names[x] not in girls:
    print(names[x] + " boy")
  elif names[x] in girls and names[x] not in boys:
    print(names[x] + " girl")
  else:
    print(names[x] + " either")
  x += 1
