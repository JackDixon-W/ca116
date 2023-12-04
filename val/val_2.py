#!/usr/bin/env python3

while True:
  #start = 0
  N = int(input("Input any number N as the end the range "))

  print("the prime are:")
  sum = 0
  for i in range(2, N + 1):
    for j in range(2, i):
      if i % j == 0:
        break
    else:
      print(i, end = ", ")
      i = i ** 2
      sum = sum + i
  print("and..\n""The sum of the squares of these primes is", sum, "!!!")

  while True:
    answer = str(input("\n Would you like to try again? (y/n) "))
    if answer in ("y", "n"):
      break
    print("invalid input")
  if answer == "y":
    continue
  else:
    print("Goodbye")
    break
