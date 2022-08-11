class LineGrid:
  def __init__(self, x, y):
    self.grid = [ [0] * x for i in range(y) ]

  def _drawToCell(self, x, y):
    self.grid[y][x] += 1

  def _drawHorizontalLine(self, y, x1, x2):
    xVals = list(range(min(x1, x2), max(x1, x2)+1))

    for x in xVals:
      self._drawToCell(x, y)

  def _drawVerticalLine(self, x, y1, y2):
    yVals = list(range(min(y1, y2), max(y1, y2)+1))

    for y in yVals:
      self._drawToCell(x, y)

  def _calcDrawDirections(self, p1, p2):
    xDir = 0
    yDir = 0
    if (p2[0] - p1[0] > 0):
      xDir = 1
    else:
      xDir = -1

    if (p2[1] - p1[1] > 0):
      yDir = 1
    else:
      yDir = -1

    return (xDir, yDir)
  
  def _drawDiagonalLine(self, p1, p2):
    drawDirections = self._calcDrawDirections(p1, p2)
    xRange = list(range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1))
    yRange = list(range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1))

    if (drawDirections[0] < 0):
      xRange.reverse()
    if (drawDirections[1] < 0):
      yRange.reverse()

    if len(xRange) != len(yRange):
      return

    for i in range(len(xRange)):
      self._drawToCell(xRange[i], yRange[i])

    # for y in yRange:
    #   for x in xRange:
    #     self._drawToCell(x, y)
  
  def _checkForTrueDiagonal(self, p1, p2):
    if (p1[1] == p2[1]): return False

    return abs((p2[0] - p1[0]) / (p2[1] - p1[1])) == 1

  def _countDrawnPoints(self):
    count = 0

    for y in range(0, len(self.grid)-1):
      for x in range(0, len(self.grid[y])-1):
        if self.grid[y][x] > 0:
          count += 1

    return count

  def countIntersections(self):
    count = 0

    for y in range(0, len(self.grid)-1):
      for x in range(0, len(self.grid[y])-1):
        if self.grid[y][x] > 1:
          count += 1

    return count
  
  def drawLine(self, segment):
    point1 = segment[0]
    point2 = segment[1]
    isHorizontal = point1[1] == point2[1]
    isVertical = point1[0] == point2[0]
    isDiagonal = self._checkForTrueDiagonal(point1, point2)

    if not isHorizontal and not isVertical:
      if isDiagonal:
        self._drawDiagonalLine(point1, point2)
      else:
        return
    else:
      if isHorizontal:
        self._drawHorizontalLine(point1[1], point1[0], point2[0])
      elif isVertical:
        self._drawVerticalLine(point1[0], point1[1], point2[1])
