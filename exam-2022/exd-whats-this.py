#!/usr/bin/env python3

p = input()
w = input()

if len(p) != len(w):
  print("no")
else:
  i = 0
  while i < len(w) and (w[i] == p[i] or p[i] == "-"):
    i = i + 1

  if i < len(w):
    print("no")
  else:
    print("yes")
