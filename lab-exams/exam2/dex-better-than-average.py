#!/usr/bin/env python3

import sys
users = sys.stdin.read().split("\n")
users = users[:len(users) - 1]

i = 0
average = 0
while i < len(users):
  average += int(users[i][len(users[i]) - 2:])
  i += 1

average = average // len(users)
i = 0
while i < len(users):
  if int(users[i][len(users[i]) - 2:]) > average:
    print(users[i][:len(users[i]) - 3])
  i += 1
