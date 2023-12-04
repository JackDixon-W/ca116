#!/usr/bin/env python3

i = 0
n = input()
numbers = []
highest = 0

#Store everything as part of a list
#Remember 0 does count as an acceptable input
#Use the index number as the number input
#And the number stored at that index value as the frequency
#The question is how do I make a list long enough to take any variable
#Also, do I have to be able to take any variable or can I just take
#Single digit variables

#Solution:
#Take all the numbers into an array first, use that array length as
#The length of the histogram array

while n != "end":
  numbers.append(int(n))
  if int(n) > highest:
    highest = int(n)
  n = input()
  i += 1

histogram = [0] * (highest + 1)
j = 0
while j < i:
  histogram[numbers[j]] += 1
  j += 1

k = 0
while k < highest + 1:
  print(k, "*" * histogram[k])
  k += 1

if k == 1:
  while k < 10:
    print(k, "")
    k += 1
