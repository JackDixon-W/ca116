#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

if a + b > c and c >= a and c >= b:
  print("yes")
elif a + c > b and b >= a and b >= c:
  print("yes")
elif b + c > a and a >= b and a >= c:
  print("yes")
else:
  print("no")
