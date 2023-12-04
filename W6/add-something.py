#!/usr/bin/env python3

i = 0
x = []
n = input()

while n != "end":
  x.append(int(n))
  n = input()

j = int(input())
while i < len(x):
  print(x[i] + j)
  i += 1
