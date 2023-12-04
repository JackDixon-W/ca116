#!/usr/bin/env python3

s = input()
i = 0
j = 0
day = ""
num = ""
month = ""
year = ""


while i < len(s) and s[i] != " ":
  day += s[i]
  i += 1

i += 1
while i < len(s) and s[i] != " ":
  num += s[i]
  i += 1
i += 1

while i < len(s) and s[i] != ",":
  month += s[i]
  i += 1
i += 2

while i < len(s):
  year += s[i]
  i += 1

#if len(num) == 1:
#  num += "st"
#elif num[len(num) - 2] == "1":
#  num += "th"
#elif num[len(num) - 1] == "3":
#  num += "rd"
#elif num[len(num) - 1] == "1":
#  num += "st"
#elif num[len(num) - 1] == "2":
#  num += "nd"
#else:
#  num += "th"

print(month + " " + num + ", " + year + " (" + day + ")")
