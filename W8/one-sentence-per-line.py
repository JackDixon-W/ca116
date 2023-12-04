#!/usr/bin/env python3

n = input()
i = 0
data = []
extra = []

while n != "end":
  data.append(n)
  n = input()

full = "\n".join(data)
full = full.strip()
words = full.split()
out = ""

while i < len(words):
  if "." in words[i] and not i == len(words) - 1:
    j = 0
    while j + 1 < len(words[i]):
      if words[i][j] == ".":
        words[i] = words[i][:j + 1] + "\n" + words[i][j + 1:]
      j += 1
    if not "\n" in words[i]:
      words[i] += "\n"
  if not words[i][len(words[i]) - 1] == "\n":
    out += words[i] + " "
  else:
    out += words[i]
  i += 1

print(out)
