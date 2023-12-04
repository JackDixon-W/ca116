#!/usr/bin/env python3

import sys

inp = sys.stdin.read().split()
inputArray = inp[:len(inp) - 1]
i = 0

#Can only have 2 loops
#Loop 1 = Finds biggest
#Initialise a new list of length "max + 1"
#Loop 2 = stores the frequency of each number
#countArray[i] = countArray[i-1] + countArray[i]
max = int(inputArray[0])
lng = len(inputArray)
while i < len(inputArray) * 2:
  if i >= len(inputArray):
    countArray[i - lng] = countArray[i - 1 - lng] + countArray[i - lng]
  else:
    if int(inputArray[i]) > max:
      max = int(inputArray[i])
    countArray = [0] * (max + 1)
    outputArray = [0] * (len(inputArray))
  i += 1

i = 0
while i < len(inputArray):
  outputArray[int(countArray[int(inputArray[i])]) - 1 ] = inputArray[i]
#  outputArray[int(countArray[int(inputArray[i])] - 1] = inputArray[i]
  countArray[int(inputArray[i])] = countArray[int(inputArray[i])]
  print(countArray)
  print(outputArray)
  i += 1

print(outputArray)
#i = 6
#countArray[countArray[inputArray[6]]-1] = inputArray[6]
#countArray[inputArray[6]] = countArray[inputArray[6]]
