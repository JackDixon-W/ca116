#!/usr/bin/env python3

i = 0
j = 0
n = input()
ans = ""

while i < len(n):
  #Every 2nd letter should be capital
  #In Python that means every even letter
  if n[i] >= "A" and n[i] <= "Z" or n[i] >= "a" and n[i] <= "z":
    j += 1
  if j % 2 == 1:
    if n[i] >= "A" and n[i] <= "Z":
      ans += chr(ord(n[i]) + 32)
    else:
      ans += n[i]
  else:
    if n[i] >= "a" and n[i] <= "z":
      ans += chr(ord(n[i]) - 32)
    else:
      ans += n[i]
  i += 1

print(ans)
