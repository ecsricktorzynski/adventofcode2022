import numpy as np

# dictionary for mapping to matrix
rps_dict = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2 }

# define matrix for 1st day
rps_matrix = np.array([[4, 8, 3], [1, 5, 9], [7, 2, 6]])

# define matrix for 2nd day
rps_matrix2 = np.array([[3, 4, 8],[1, 5, 9], [2, 6, 7]])

score = 0
score2 = 0

# open the file in read mode
file = open("input2.txt", "r")

# read the lines of the file as a list
lines = file.readlines()

# iterate over the lines of the file
for line in lines:
    # remove the carriage return
    line = line.rstrip()
    
    # split the lines
    elf, _, me = line.partition(" ")
    
    # get the value from dict
    X = rps_dict[elf]
    Y = rps_dict[me]
    
    # add the score in
    score = score + rps_matrix[X, Y]
    score2 = score2 + rps_matrix2[X, Y]

# close the file
file.close()

print(f"Score day 1: {score}") 
print(f"Score day 2: {score2}")