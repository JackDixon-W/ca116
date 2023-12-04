#!/usr/bin/env python3

import os
import shutil

files = os.listdir(".")

i = 0
while i < len(files):
  if os.path.isfile(files[i]) and files[i][len(files[i]) - 4:] != ".bak":
    shutil.copy2(files[i], files[i] + ".bak")
  i += 1
