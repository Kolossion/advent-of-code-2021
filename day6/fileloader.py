def loadLines(filepath):
  inputFile = open(filepath, 'r')
  lines = map(str.rstrip, inputFile.readlines())
  return list(lines)