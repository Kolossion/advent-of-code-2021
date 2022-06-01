inputFile = open('./day1/input.txt','r')
lines = inputFile.readlines()
count = 0

# part 1
# for i in range(len(lines)):
#   if i == 0: continue

#   number = int(lines[i])
#   prevNumber = int(lines[i-1])
#   if (number > prevNumber):
#     count += 1

# part 2
for i in range(len(lines)):
  if i == 0: continue
  if i+2 >= len(lines) or i+1 >= len(lines): continue

  number = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
  prevNumber = int(lines[i-1]) + int(lines[i]) + int(lines[i+1])
  if (number > prevNumber):
    count += 1

print(count)