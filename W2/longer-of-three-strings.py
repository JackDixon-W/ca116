#!/usr/bin/env python3

inp1 = input()
inp2 = input()
inp3 = input()

if len(inp1) > len(inp2) and len(inp1) > len(inp3):
  print(inp1)
elif len(inp2) > len(inp3) and len(inp2) > len(inp1):
  print(inp2)
else:
  print(inp3)
