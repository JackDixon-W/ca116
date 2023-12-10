#!/usr/bin/env python3

servers = []

s = input()
while s != "end":
  n = int(s)
  if len(servers) == 0:
    servers.append(n + 1000)
  else:
    updated = False
    i = 0
    while i < len(servers) and not updated:
      if n >= servers[i]:
        servers[i] = n + 1000
        updated = True
      i += 1
    if not updated:
      servers.append(n + 1000)
  s = input()
print(len(servers))
