def findIslands(grid):
  if not grid:
    return 0
  ctr = 0
  isVisited = [[False]*len(grid) for x in range(len(grid[0]))]
  row_len = len(grid)
  col_len = len(grid[0])
  for i in range(row_len):
      for j in range(col_len):
          #print('i,j::::',i,j)
          if grid[i][j] == 1 and not isVisited[i][j]:
              ctr += 1
              findIslandsHelp(grid, i, j, row_len, col_len, isVisited)
  return ctr

def findIslandsHelp(grid, i, j, row_len, col_len, isVisited):
    # import pdb; pdb.set_trace()
    #print('i,j:',i,j)
    if i < 0 or j < 0 or i >= row_len or j >= col_len or isVisited[i][j] or grid[i][j]==0:
        return
    isVisited[i][j] = True
    findIslandsHelp(grid, i, j+1, row_len, col_len, isVisited)
    findIslandsHelp(grid, i+1, j, row_len, col_len, isVisited)
    findIslandsHelp(grid, i, j-1, row_len, col_len, isVisited)
    findIslandsHelp(grid, i-1, j, row_len, col_len, isVisited)

grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

res = findIslands(grid)
print(res)
