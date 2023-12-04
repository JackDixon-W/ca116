#!/usr/bin/env python3

n = input()
i = 0
j = 0
a = []
b = []

while n != "end":
  a.append(int(n))
  n = input()

n = input()
while n != "end":
  b.append(int(n))
  n = input()

while i < len(a) and j < len(b):
  if a[i] < b[j]:
    print(a[i])
    i += 1
  else:
    print(b[j])
    j += 1

while i < len(a):
  print(a[i])
  i += 1

while j < len(b):
  print(b[j])
  j += 1
