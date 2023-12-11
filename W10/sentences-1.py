#!/usr/bin/env python3

import sys

inp = sys.stdin.read()
lib = {".": ".", "!": "!", "?": "?"}

i = 0
output = ""
while i < len(inp):
  output += inp[i]
  if inp[i] in lib and (inp[i + 1] == " " or inp[i + 1] == "\n"):
    output = ' '.join(output.split())
    print(output)
    output = ""
  i += 1
