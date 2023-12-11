#!/usr/bin/env python3

import sys

inp = sys.stdin.read()
lib = {".": ".", "!": "!", "?": "?"}
caps = {}

x = ord("A")
i = 0
while i < 26:
  caps[chr(x)] = True
  i += 1
  x += 1

i = 0
output = ""
while i < len(inp):
  output += inp[i]
  if inp[i] in lib and (inp[i + 1] == " " or inp[i + 1] == "\n"):
    output = ' '.join(output.split())
    j = 0
    saved = []
    while j < len(output):
      if output[j] in caps:
        saved.append(j)
        saved.append(output[j])
      j += 1
    output = output.capitalize()
    j = 0
    while j < len(saved):
      temp_l = output[:saved[j]]
      temp_r = output[saved[j] + 1:]
      temp_m = saved[j + 1]
      output = temp_l + temp_m + temp_r
      j += 2
    print(output)
    output = ""
  i += 1
