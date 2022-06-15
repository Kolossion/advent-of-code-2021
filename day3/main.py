inputFile = open('./day3/input.txt', 'r')
lines = inputFile.readlines()

gamma = 0
gammaBitStr = ''
# gammaList = []
epsilon = 0
epsilonBitStr = ''
# epsilonList = []
bitFreq0 = []
bitFreq1 = []

bitWidth = len(lines[0].strip())
bitFreq0 = [0] * bitWidth
bitFreq1 = [0] * bitWidth

for line in lines:
  # print("HEY:", line)
  binary = line.strip()

  for i in range(len(binary)):
    bit = binary[i]
    bitVal = int(bit)

    if (bitVal == 0):
      bitFreq0[i] += 1
    elif (bitVal == 1):
      bitFreq1[i] += 1

for i in range(len(bitFreq0)):
  if (bitFreq1[i] > bitFreq0[i]):
    gammaBitStr += '1'
    epsilonBitStr += '0'
  else:
    gammaBitStr += '0'
    epsilonBitStr += '1'

gamma = int(gammaBitStr, 2)
epsilon = int(epsilonBitStr, 2)

print("GAMMA", gamma)
print("EPSILON", epsilon)
print("POWER CONSUMPTION", gamma * epsilon)