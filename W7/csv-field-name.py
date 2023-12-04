#!/usr/bin/env python3

import sys

position = int(sys.argv[1])
i = 0
j = 0
n = input()

while j < position:
  while n[i] != "," and i < len(n):
    i += 1
  j += 1
  i += 1

j = i
while j < len(n) and n[j] != ",":
  j += 1

print(n[i:j])
