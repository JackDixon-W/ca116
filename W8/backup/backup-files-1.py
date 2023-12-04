#!/usr/bin/env python3

import os
import shutil
files = os.listdir(".")
backup = []

i = 0
while i < len(files):
  if files[i][len(files[i]) - 4:] != ".bak":
    backup.append(files[i])
  i += 1

i = 0
while i < len(backup):
  shutil.copy2(backup[i], backup[i] + ".bak")
  i += 1
