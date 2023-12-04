#!/usr/bin/env python3

n = input()
i = 0
data = []

while n != "end":
  data.append(n)
  n = input()

hours = 0
while i < len(data):
  cur_hour = data[i].split()
  hours += int(cur_hour[2])
  i += 1

print(hours)
