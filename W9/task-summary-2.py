#!/usr/bin/env python3

import sys

list = sys.stdin.read().split("\n")
list = list[:len(list) - 1]

#Dictionary can store 2 things
#Key = User
#Value = Task or Correctness or Count
#Make 2 dictionaries?
#Dic 1 = User : Count
#Dic 2 = User-task : Correctness
#Use dic 2 to make dic 1?

user_task = {}
count = {}

line = 0
while line < len(list):
  pos = 0
  cur = list[line]
  while pos < len(cur) and cur[pos] != ".":
    pos += 1
  pos += 1
  while pos < len(cur) and cur[pos] != ".":
    pos += 1
  if cur[pos + 1] == "c":
    user_task[cur[:pos]] = True
  else:
    user_task[cur[:pos]] = False
  line += 1

for setup in user_task:
  pos = 0
  while pos < len(setup) and setup[pos] != "/":
    pos += 1
  count[setup[:pos]] = 0

for keys in user_task:
  pos = 0
  while pos < len(keys) and keys[pos] != "/":
    pos += 1
  slash_pos = pos
  if user_task[keys] is True:
    count[keys[:slash_pos]] += 1

for keys in count:
  print(keys, count[keys])
