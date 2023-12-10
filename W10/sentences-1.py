#!/usr/bin/env python3

import sys

inp = sys.stdin.read()

i = 0
while i < len(inp):
  if inp[i] == "." and (inp[i + 1] == " "):
    
