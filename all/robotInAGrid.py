def robotInAGrid(maze):
  if maze:
    path = []
    mydict = {}
    if getPath(maze, len(maze)-1, len(maze[0])-1, path, mydict):
      print(mydict)
      return path

def getPath(maze, row, col, path, mydict):
  if row < 0 or col < 0 or not maze:
    return False
  if (row,col) in mydict:
    return mydict[(row,col)]
  elif (row == 0 and col == 0) or getPath(maze, row-1, col, path, mydict) or getPath(maze, row, col-1, path, mydict):
    path.append((row,col))
    mydict[(row,col)] = True
    return True
  return False

maze = [[1,2,3],[4,5,6],[7,8,9]]
res = robotInAGrid(maze)
print(res)
