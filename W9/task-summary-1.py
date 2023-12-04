#!/usr/bin/env python3

import sys

tasks = sys.stdin.read().split()
log = {}

i = 0
while i < len(tasks):
  j = 0
  while tasks[i][j] != ".":
    j += 1
  tag = tasks[i][j + 4:]
  name = tasks[i][:j + 3]
  if tag == "correct":
    log[name] = True
  else:
    log[name] = False
  i += 1

for key in log:
  if log[key] is True:
    print(key)
