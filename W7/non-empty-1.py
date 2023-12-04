#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["dog", "cat", "mouse", "", "test", "", "test"]

i = 0
count = 0
while i < len(a):
  if not a[i] == "":
    count += 1
  i += 1

print(count)
