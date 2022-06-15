
inputFile = open('./day3/input.txt', 'r')
lines = inputFile.readlines()

oxygenRating = 0
scrubberRating = 0

bitWidth = len(lines[0].strip())

def calcScrubberRating():
  workingList = lines
  popBit = 0
  idx = 0

  while True:
    popBit = getMinorityAtBitIndex(workingList, idx)

    workingList = getSublist(workingList, idx, popBit)

    if (len(workingList) == 1): break
    idx += 1
  
  return int(workingList[0], 2)

def calcOxygenRating():
  workingList = lines
  popBit = 0
  idx = 0


  while True:
    popBit = getMajorityAtBitIndex(workingList, idx)
    workingList = getSublist(workingList, idx, popBit)

    if (len(workingList) == 1): break
    idx += 1
  
  return int(workingList[0], 2)
    

def getSublist(list, bitIdx, bit):
  newList = []

  for num in list:
    if (int(num[bitIdx]) == bit):
      newList.append(num)

  return newList

def countBitFreq(list):
  ones = 0
  zeroes = 0

  for bit in list:
    if (int(bit) == 0):
      zeroes += 1
    elif (int(bit) == 1):
      ones += 1
  
  return [zeroes, ones]

def getMinorityAtBitIndex(curList, index):
  bitListAtIndex = list(map(lambda val : val[index], curList))
  counts = countBitFreq(bitListAtIndex)

  if (counts[0] <= counts[1]):
    return 0
  else:
    return 1

def getMajorityAtBitIndex(curList, index):
  bitListAtIndex = list(map(lambda val : val[index], curList))
  counts = countBitFreq(bitListAtIndex)

  if (counts[0] <= counts[1]):
    return 1
  else:
    return 0

oxygenRating = calcOxygenRating()
scrubberRating = calcScrubberRating()

print("Oxygen Rating", oxygenRating)
print("CO2 Scrubber Rating", scrubberRating)
print("LIFE SUPPORT", oxygenRating * scrubberRating)