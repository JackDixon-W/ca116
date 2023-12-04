#!/usr/bin/env python3

import sys
n = int(sys.argv[1])

middle = n // 2 + 1

i = 0
while i < middle:
    print(" " * (middle - i - 1) + "*" * (i * 2 + 1))
    i += 1

i = middle - 2
while i >= 0:
    print(" " * (middle - i - 1) + "*" * (2 * i + 1))
    i -= 1
