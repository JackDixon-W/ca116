#!/usr/bin/env python3

s = input()

print(s[len(s) - 1:len(s)] + s[1:len(s) - 1] + s[0:1])
