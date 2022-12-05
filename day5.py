# Day 5
moved_box = ""

stack = list([list("BVSNTCHQ"),list("WDBG"),list("FWRTSQB"),
  list("LGWSZJDN"),list("MPDVF"),list("FWJ"),list("LNQBJV"),
  list("GTRCJQSN"),list("JSQCWDM")])

print(stack)
# function to move the boxes
def move_boxes(stack, move_num, move_from, move_to):
  # number of moves to make
  for m in range(1,move_num+1):

    # pop the last crate off the stack
    moved_box = stack[move_from].pop()

    # push the crate onto the new stack
    stack[move_to].append(moved_box)
   
  return(stack)

# open the file in read mode
file = open("input5.txt", "r")

# read the lines of the file as a list
lines = file.readlines()

line_val = []

# iterate over the lines of the file
for line in lines:
    # remove the carriage return
    line = line.rstrip()
    
    # parse the line
    line_val = line.split()
    move_num = int(line_val[1])
    move_from = int(line_val[3])-1
    move_to = int(line_val[5])-1

    # move the boxes
    stack = move_boxes(stack, move_num, move_from, move_to)

code = ""
char = ""
print(stack)
# pop the stacks to get the code
for i in range (0,9):
  char = str(stack[i].pop())
  code = code + char
  
print(f"code = {code}")