import fileloader as fl
from linegrid import LineGrid

def pointStrToTuple(pointStr):
  coords = pointStr.split(',')
  return (int(coords[0]), int(coords[1]))

def processRawLine(line):
  points = line.split(' -> ')
  segment = list(map(pointStrToTuple, points))
  return segment

def main():
  data = fl.loadLines('./day5/input.txt')
  grid = LineGrid(1000, 1000)
  lineSegments = list(map(processRawLine, data))

  # grid.drawLine(lineSegments[0])
  for segment in lineSegments:
    grid.drawLine(segment)
    
  print(grid._countDrawnPoints())
  print(grid.countIntersections())

if __name__ == "__main__":
  main()