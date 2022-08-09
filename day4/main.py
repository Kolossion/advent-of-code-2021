from board import BingoBoard

inputFile = open('./day4/input.txt', 'r')
lines = inputFile.readlines()
picks = []
boards = []
winningScore = 0

def setPicks(pickStr):
  global picks
  picks = pickStr.strip().split(',')

def createBoards():
  firstIdx = 2
  curIdx = firstIdx
  boardSize = 5

  while True:
    result = createBoard(curIdx, curIdx + boardSize - 1)
    if result == -1: break
    curIdx = curIdx + boardSize + 1

def createBoard(idx, endIdx):
  rows = []

  if (idx >= len(lines) or endIdx >= len(lines)):
    return -1

  for i in range(idx, endIdx + 1):
    rows.append(lines[i].strip().split())

  board = BingoBoard(rows)
  boards.append(board)

  return 0

def applyPick(num):
  for board in boards:
    board.markNumber(num)

def checkForWins():
  for boardIdx in range(len(boards)):
    if (boards[boardIdx].checkForWin() != False):
      return boardIdx
  
  return -1

def getScore(winIdx):
  return boards[winIdx].getScore()

def main():
  global winningScore
  setPicks(lines[0])
  createBoards()

  for pick in picks:
    print("PICKING: ", pick)
    applyPick(pick)
    win = checkForWins()
    while win != -1 and len(picks) >= 1:
      print("WINNING INDEX", win)
      if len(boards) == 1:
        print("WINNING BOARD:", boards[win])
        print("BOARDS", boards)
        winningScore = getScore(win)
        print("WINNING SCORE", winningScore)
    
      boards.pop(win)

      win = checkForWins()

    # if win != -1:
    #   winningScore = getScore(win)
    #   break
  
  print("WINNING SCORE:", winningScore)
  

if __name__ == "__main__":
  main()