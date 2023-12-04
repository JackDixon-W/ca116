#!/usr/bin/env python3

i = 0
n = input()
j = 0

while i < len(n) and (n[i] < "0" or n[i] > "9"):
  i += 1

while i < len(n) and (n[i] >= "0" and n[i] <= "9"):
  i += 1

while i < len(n) and (n[i] < "0" or n[i] > "9"):
  i += 1

j = i
while i < len(n) and (n[i] >= "0" and n[i] <= "9"):
  i += 1

if j != len(n) and (n[j] >= "0" and n[j] <= "9"):
  print(n[j:i], j)
