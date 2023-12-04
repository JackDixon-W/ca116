#!/usr/bin/env python3

import os
import shutil
files = os.listdir(".")
backup = []

i = 0
while i < len(files):
  if os.path.isfile(files[i]) and files[i][len(files[i]) - 4:] == ".bak":
    backup.append(files[i])
  i += 1

i = 0
while i < len(backup):
  os.remove(backup[i])
  i += 1
