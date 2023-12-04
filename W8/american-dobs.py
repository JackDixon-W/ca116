#!/usr/bin/env python3

with open("irish-dobs.txt") as f:
  lines = f.readlines()
  i = 0
  with open("american-dobs.txt", "w") as x:
    while i < len(lines):
      full = lines[i].split()
      cur = full[0].split("/")
      temp = cur[0]
      cur[0] = cur[1]
      cur[1] = temp
      new = "/".join(cur[:3])
      names = " ".join(full[1:])
      dates = "/".join(cur)
      x.write(dates + " " + names + "\n")
      i += 1
