h_pos = 0
depth = 0
aim = 0

inputFile = open('./day2/input.txt', 'r')
lines = inputFile.readlines()

def inputCommand(word, val): 
  global h_pos, depth, aim

  if (word=='forward'):
    h_pos += int(val)
    depth += (aim * int(val))
  elif (word =="up"):
    # depth -= int(val)
    aim -= int(val)
  elif (word == "down"):
    # depth += int(val)
    aim += int(val)


for i in range(len(lines)):
  parts = lines[i].split()
  inputCommand(parts[0], parts[1])

print("HORIZ: ", h_pos)
print("DEPTH: ", depth)
print("DEPTH * HORIZ: ", h_pos * depth)