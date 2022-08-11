import fileloader as fl

# ============ NAIVE IMPLEMENTATION =========
# def minusOne(val):
#   return val - 1

# def step(t, state):
#   numBirths = 0

#   reduced = list(map(minusOne, state))
#   for i in range(len(reduced)):
#     if reduced[i] == -1:
#       numBirths += 1
#       reduced[i] = 6

#   nextState = reduced + ([8] * numBirths)

#   return nextState

# def main():
#   runs = 256

#   data = fl.loadLines('./day6/input.txt')
#   inputList = data[0].split(',')
#   inputList = list(map(int, inputList))

#   fish = inputList

#   for t in range(runs):
#     fish = step(t, fish)

#   print("NUM FISH:", len(fish))
# ===========================================

def step(t, list):
  births = list.pop(0)
  list[6] += births
  list.append(births)

  return list

def processInput(inputList):
  output = [0] * 9

  for i in range(len(inputList)):
    output[int(inputList[i])] += 1

  return output


def main():
  runs = 256

  data = fl.loadLines('./day6/input.txt')
  inputList = data[0].split(',')
  inputBucketList = processInput(inputList)
  # inputList = list(map(int, inputList))
  print(inputBucketList)

  fish = inputBucketList

  for t in range(runs):
    fish = step(t, fish)

  print("NUM FISH:", sum(fish))
  # print("NUM FISH:", len(fish))

if __name__ == "__main__":
  main()