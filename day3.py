import numpy as np

# create priority dictionary
chararr = []
characters = ""
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chararr = [c for c in characters]

priority = 0
priority_dict = {}
priority_sum = 0

for char in chararr:
  priority = priority + 1
  priority_dict[char] = priority

linelength = 0

# open the file in read mode
file = open("input3.txt", "r")

# read the lines of the file as a list
lines = file.readlines()

# iterate over the lines of the file
for line in lines:
    # remove the carriage return
    line = line.rstrip()
    
    # split the lines
    linelength = len(line)
    
    rugsack1 = line[:len(line)//2]
    rugsack2 = line[len(line)//2:]
    
    rugsack1_arr = [c for c in rugsack1]
    rugsack2_arr = [c for c in rugsack2]

    # print(f"rugsack1_arr = {rugsack1_arr}")
    # print(f"rugsack2_arr = {rugsack2_arr}")

    for item in rugsack1_arr:
      if item in rugsack2_arr:
        priority_sum = priority_sum + priority_dict[item]
        break
    
# close the file
file.close()

print(f"Priority sum = {priority_sum}")