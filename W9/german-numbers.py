#!/usr/bin/env python3

import sys

german = "eins zwei drei vier funf sechs sieben acht neun zehn".split()
english = "one two three four five six seven eight nine ten".split()
dictionary = {}

j = 0
while j < 10:
  dictionary[english[j]] = german[j]
  j += 1

words = sys.stdin.read().split()
i = 0
while i < len(words):
  print(dictionary[words[i]])
  i += 1
