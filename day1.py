# open the file in read mode
file = open("input1.txt", "r")

# read the lines of the file as a list
lines = file.readlines()
caloriecount = 0
elf = []

# iterate over the lines of the file
for line in lines:
    # remove the carriage return
    line = line.rstrip()
    
    if (line):
      caloriecount = caloriecount + int(line)
    else:
      elf.append(caloriecount)
      caloriecount = 0

# close the file
file.close()

elfmax = max(elf)
print(f"Maximum calorie count = {elfmax}")


# Star 2
sorted_elves = sorted(elf, reverse=True)

# add up first 3 elves

top3elves = sorted_elves[0] + sorted_elves[1] + sorted_elves[2]
print(f"Sum of calorie count for first 3 elves: {top3elves}")