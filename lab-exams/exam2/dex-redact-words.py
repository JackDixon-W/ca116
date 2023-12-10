#!/usr/bin/env python3

import sys
redact = sys.argv[1:]
words = sys.stdin.read().split()

i = 0
while i < len(words):
  if words[i] in redact:
    print("*" * len(words[i]))
  else:
    print(words[i])
  i += 1
