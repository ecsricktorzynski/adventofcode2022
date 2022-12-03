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

# initialize array
rugsack_arr = [[] for _ in range(len(lines))]
  
# iterate through groups of 3
for i in range(0, len(lines), 3):
  rugsack_arr[i] = [c for c in lines[i]]
  rugsack_arr[i+1] = [c for c in lines[i+1]]
  rugsack_arr[i+2] = [c for c in lines[i+2]]
 
  for item in rugsack_arr[i]:
    if item in rugsack_arr[i+1] and item in rugsack_arr[i+2] :
      priority_sum = priority_sum + priority_dict[item]
      break
      
# close the file
file.close()

print(f"Priority sum = {priority_sum}")