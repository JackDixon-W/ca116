#!/usr/bin/env python3

n = input()
i = 0
data = [] #List of all data involved

while n != "end":
  data.append(n) #input is taken and appended to data list
  n = input()

while i < len(data):
  cur = data[i].split() #Cur is the current line, as a list
  start = int(cur[1]) #This is the start time as an integer
  if cur[1][0] == "0": #This checks if the time is something like 09
    cur[1] = cur[1][1] #If yes, remove the 0
  cur[1] += ":00" #Add :00 to the start time in the list
  temp = int(cur[2]) #Temp is the end time
  cur[2] = start + temp - 1 #End time = Start time + End Time - 1
  cur[2] = str(cur[2]) #End time is set to a string
  cur[2] += ":50" #End time has :50 appended to it
  print(" ".join(cur)) #The line is printed with all elements joined
  i += 1
