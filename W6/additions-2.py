#!/usr/bin/env python3

i = 0
start = 0
j = "0"
k = "0"
z = "0"
m = "0"
x = "0"
n = input()
total = 0

while i < len(n):
  while i < len(n) and n[i] != "+":
    i += 1
  if j == "0":
    j = n[0:i]
    start = i
  elif k == "0":
    k = n[start + 1:i]
    start = i
  elif z == "0":
    z = n[start + 1: i]
    start = i
  elif m == "0":
    m = n[start + 1: i]
    start = i
  else:
    x = n[start + 1:]
  i += 1

total = int(j) + int(k) + int(z) + int(m) + int(x)
print(total)
