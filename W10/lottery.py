#!/usr/bin/env python3

import sys
winners_list = sys.argv[1:]
winners = {winners_list[0]: True, winners_list[1]: True, winners_list[2]: True}

inp = sys.stdin.readlines()
i = 0
while i < len(inp):
  cur = inp[i]
  if len(cur[2]) == 3:
    cur[2] = cur[2][0]
  elif len(cur[2]) == 4:
    cur[2] = cur[2][0:2]
  j = 0
  balls = 0
  while j < 4:
    if cur[j] in winners:
      balls += 1
    j += 1
  prize = 0
  if balls == 0:
    prize = 0
  elif balls == 1:
    prize = 1
  elif balls == 2:
    prize = 5
  elif balls == 3:
    prize = 100
  print(prize)
  i += 1
