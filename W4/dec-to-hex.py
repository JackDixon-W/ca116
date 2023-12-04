#!/usr/bin/env python3

n = int(input())

# Numbers start at 48 (48 = 0)
# Letters start at 65 (65 = A)
# It allows the hex function?

hex = hex(n)
hex = str(hex)
print(hex[2:len(hex)])
