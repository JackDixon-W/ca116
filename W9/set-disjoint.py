#!/usr/bin/env python3

with open("a.txt") as a:
  lines1 = a.read().split("\n")
  lines1 = lines1[:len(lines1) - 1]

with open("b.txt") as b:
  lines2 = b.read().split("\n")
  lines2 = lines2[:len(lines2) - 1]

seen = {}
i = 0
while i < len(lines1):
  seen[lines1[i]] = True
  i += 1

j = 0
while j < len(lines2):
  seen[lines2[j]] = False
  j += 1

if i + j > len(seen):
  print("intersecting")
else:
  print("disjoint")
