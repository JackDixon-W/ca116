#!/usr/bin/env python3

import os
files = os.listdir(".")

i = 0
while i < len(files):
  if files[i][len(files[i]) - 3:] == ".py":
    print(files[i])
  i += 1
