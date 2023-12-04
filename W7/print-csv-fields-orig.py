#!/usr/bin/env python3

i = 0
n = input()
inps = []

while n != "end":
  inps.append(n)
  n = input()

#You are going to have to revisit some of the ideas in this code
#I'm not sure if nesting the while statements is entirely necessary
#Eg. while k < n (Line 23)
#This line simply will not do what was originally intended
#We want the loop to run until it hits the first comma
#So why not simply use the internal loop?

n = int(input())
j = 0
p = 0
k = 0
while i < len(inps):
  while k < n: #k = start of print
    while inps[j] != ",":
      j += 1
    k += 1
  if n != 0:
    k += 1 #Adds 1 to skip past the comma
  while l < n + 1 and l < len(inps): #l = end of print
    while inps[p] != ",":
      p += 1
    l += 1
    
