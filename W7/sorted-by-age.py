#!/usr/bin/env python3

n = input()
i = 0
names = []
dates = []
years = []

while n != "end":
  names.append(n)
  #dates.append(n[0:8])
  #years.append(n[6:8])
  n = input()

while i < len(names):
  p = i
  low = names[i][6:8]
  pos = i
  while p < len(names):
    if low > names[p][6:8]:
      low = names[p][6:8]
      pos = p
    elif low == names[p][6:8] and names[pos][3:5] > names[p][3:5]:
      low = names[p][6:8]
      pos = p
    elif low == names[p][6:8] and names[pos][3:5] == names[p][3:5]:
      if names[pos][:2] > names[p][:2]:
        low = names[p][6:8]
        pos = p
    p += 1
  temp = names[i]
  names[i] = names[pos]
  names[pos] = temp
  i += 1

i = 0
while i < len(names):
  print(names[i][9:])
  i += 1
