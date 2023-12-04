#!/usr/bin/env python3

import os
files = os.listdir(".")
shebang = "#!/usr/bin/env python3"

i = 0
while i < len(files):
  check = ""
  with open(files[i]) as f:
    check = f.readline().rstrip()
  if check != "":
    if check == shebang or files[i][len(files[i]) - 3:] == ".py":
      print(files[i])
  i += 1
