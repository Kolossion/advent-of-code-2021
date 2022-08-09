class BingoBoard:
  def __init__(self, rows):
    self.lastPick = 999
    self.board = []
    for row in rows:
      self.__addRow(row)

  def markNumber(self, number):
    self.lastPick = int(number)
    for x in range(len(self.board)):
      for y in range(len(self.board[x])):
        if (self.board[x][y].value == int(number)):
          self.board[x][y].mark()

  def checkForWin(self):
    return self.__checkVerticalWins() or self.__checkHorizontalWins()

  def getScore(self):
    print("LAST PICK", self.lastPick)
    unmarkedSum = 0
    for y in range(len(self.board)):
      for x in range(len(self.board[y])):
        if (self.board[y][x].marked == False):
          unmarkedSum += self.board[y][x].value
    
    print("SUM OF UNMARKED", unmarkedSum)

    return unmarkedSum * self.lastPick

  def __addRow(self, row):
    newRow = []
    for num in row:
      newRow.append(BingoCell(int(num)))
    self.board.append(newRow)

  def __checkVerticalWins(self):
    # Making a BIG assumption here about
    # board size

    for x in range(len(self.board[0])):
      checkRow = [self.board[0][x], self.board[1][x], self.board[2][x], self.board[3][x], self.board[4][x]]
      checkRow = list(map(lambda cell:cell.marked, checkRow))
      if checkRow.count(True) == 5:
        return True
    
    return False


  def __checkHorizontalWins(self):
    for y in range(len(self.board)):
      checkRow = list(map(lambda cell:cell.marked,self.board[y]))
      if checkRow.count(True) == 5:
        return True
    
    return False


class BingoCell:
  def __init__(self, number):
    self.marked = False
    self.value = number

  def __repr__(self):
    return "[CELL: " + str(self.value) + " MARK?: " + str(self.marked) + "]"

  def mark(self):
    self.marked = True
  
  def unmark(self):
    self.marked = False