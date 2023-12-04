#!/usr/bin/env python3

i = 0
lines = []
n = input()
lines2 = []
j = 0

# Honestly just restart the work, this is too messed up to salvage

while n != "end":
  lines.append(n)
  n = input()

while i < len(lines):
  print("i = ", i)
  lines2.append(lines[i])
  while j < len(lines):
    print("lines[j] = ", lines[j], " j = ", j)
    print("lines2[i] = ", lines2[i], " i = ", i)
    print(lines2)
    if lines2[i] in lines[j]:
      lines2[i] = "0"
      print("pop!")
    j += 1
  j = 0
  print("i += 1")
  i += 1

x = 0
while x < len(lines2):
  if lines2[i] != "0":
    print(lines2[i])
  x += 1
