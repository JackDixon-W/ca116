#!/usr/bin/env python3

inp = int(input())

if inp % 3 == 0 and inp % 5 != 0:
  print("fizz")
elif inp % 5 == 0 and inp % 3 != 0:
  print("buzz")
elif inp % 5 == 0 and inp % 3 == 0:
  print("fizz-buzz")
else:
  print(inp)
