#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

j = c % 2
#If even, j = 0
#If odd, j = 1

print(a - (a * j) + (b * j))
