#!/usr/bin/env python3

import os
files = os.listdir(".")
rem = ["./"]

i = 0
while i < len(files):
  if "." in files[i]:
    print(rem[0] + files[i])
  else:
    rem.append(rem[0] + files[i] + "/")
  i += 1

while len(rem) > 1:
  cur = rem[len(rem) - 1]
  files = os.listdir(cur)
  i = 0
  while i < len(files):
    if "." in files[i]:
      print(cur + files[i])
    else:
      rem.append(cur + files[i] + "/")
    i += 1
  rem.remove(cur)
