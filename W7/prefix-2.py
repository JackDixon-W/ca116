#!/usr/bin/env python3

if __name__ == "__main__":
  a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
  s = "mont"

i = 0
while i < len(a):
  if s in a[i]:
    print(a[i])
    i += len(a)
  i += 1
