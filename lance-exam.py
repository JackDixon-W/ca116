#!/usr/bin/env python3

import sys

st = sys.stdin.readlines()
i = 0
# Priority System required.
get = {")": "(", "]": "[", "}": "{"}
grev = {"(": ")", "[": "]", "{": "}"}
gco = {")": 0, "]": 1, "}": 2}
while i < len(st):
  ac = st[i].rstrip()
  tra = 0
  keeps = ""
  oak = []

  pri = {"(": 0, "[": 0, "{": 0}
  while tra < len(ac) and -1 not in list(pri.values()) and keeps == "":
    closer = ac[tra] in list(get.keys())
    if ac[tra] in pri:
      pri[ac[tra]] += 1
      oak.append(grev[ac[tra]])
    elif closer and len(oak) == 0 or closer and gco[ac[tra]] != gco[oak[-1]]:
      keeps = (f"{i} {tra}")
    elif closer:
      pri[get[ac[tra]]] -= 1
      oak.pop()
    tra += 1
  pin = list(pri.values())
  if keeps != "":
    print(keeps)
  elif not (0 == pin[0] and 0 == pin[1] and 0 == pin[2]):
    print(i, tra)
  i += 1
