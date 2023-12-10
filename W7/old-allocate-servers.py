#!/usr/bin/env python3
servers = []
duration = 1000

line = input()
while line != "end":
    start_time = int(line)
    # Search for a server which is available at time start_time (linear search).
    #
    i = 0
    while i < len(servers) and start_time < servers[i]:
       i += 1
    if i < len(servers):
       # We found an available server, allocate existing server i.
       #
       # This server will next be available to accept new jobs at time
       # start_time + duration.
       #
       servers[i] = start_time + duration
    else:
       # No available server was found, allocate a new server.
       #
       # It will next be available to accept new jobs at time
       # start_time + duration.
       #
       servers.append(start_time + duration)

    line = input()
# The number of servers required for this workload is now just the length of
# the server list.
#
print(len(servers))

