#!/usr/bin/env python3

n = 0
i = 2
j = 1

#It needs to divide the number by each number preceding it
#Only need to check numbers up to half of it

while n != 'end':
  print("Please input N: ")
  n = int(input())
  for i in range(i, (n // 2) + 1):
    if n == 1:
      print("1 shenanigans")
      break
    for j in range(j, i):
      if j % i != 0:
        break
        print("break")
