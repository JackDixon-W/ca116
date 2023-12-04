#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
  check = ""
  with open(files[i]) as f:
    if files[i][len(files[i]) - 3:] == ".py":
      check = f.read()
  if check != "" and files[i][len(files[i]) - 3:] == ".py":
    print(files[i])
  i += 1
