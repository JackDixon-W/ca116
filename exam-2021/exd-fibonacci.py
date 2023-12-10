#!/usr/bin/env python3

num1 = 0
num2 = 1
num3 = 0

num = int(input())
while num3 < num:
  num3 = num1 + num2
  temp = num2
  num2 = num3
  num1 = temp

if num3 == num:
  print("yes")
else:
  print("no")

