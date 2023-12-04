#!/usr/bin/env python3

import sys

args = sys.argv[1]
#args = sys.stdin.read()

#Setting all non-essential variables to blank
port = ""
path = ""
query_string = ""
fragment = ""

search_pos = 0
#Find the scheme
while args[search_pos] != ":":
  search_pos += 1
scheme = args[:search_pos]

search_pos += 3
start_pos = search_pos
#Checking for a port
if ":" in args[search_pos:]:
  while args[search_pos] != ":":
    search_pos += 1
  host = args[start_pos:search_pos]

  search_pos += 1
  start_pos = search_pos
  while args[search_pos] != "/":
    search_pos += 1
  port = args[start_pos:search_pos]

else:
  while args[search_pos] != "/":
    search_pos += 1
  host = args[start_pos:search_pos]
#We now have scheme, host and port
#All after here is optional (contrary to the doc)

start_pos = search_pos
search_pos += 1
if start_pos < len(args):
  if "/" in args[start_pos:]:
    temp_hash = 0
    while search_pos < len(args) and args[search_pos] != "?":
      if args[search_pos] == "#":
        temp_hash = search_pos + 1
      search_pos += 1
    if temp_hash == 0:
      path = args[start_pos:search_pos]
    else:
      path = args[start_pos:temp_hash - 1]

    search_pos += 1
    start_pos = search_pos
    if search_pos < len(args):
      while search_pos < len(args) and args[search_pos] != "#":
        search_pos += 1
      query_string = args[start_pos:search_pos]

fragment = ""
if temp_hash != 0:
  fragment = args[temp_hash:]
elif "#" in args:
  fragment = args[search_pos + 1:len(args)]

print("scheme: " + scheme)
print("host: " + host)
if port != "":
  print("port: " + port)
if path != "":
  print("path: " + path)
if query_string != "":
  print("query-string: " + query_string)
if fragment != "":
  print("fragment-id: " + fragment)
