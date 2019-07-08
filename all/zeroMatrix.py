def zeroMatrix(mymatrix):
  if mymatrix:
    rows_with_zero = [False] * len(mymatrix)
    cols_with_zero = [False] * len(mymatrix[0])
    for i in range(len(mymatrix)):
      for j in range(len(mymatrix[0])):
        if mymatrix[i][j] == 0:
          rows_with_zero[i] = True
          cols_with_zero[j] = True
    for i in range(len(mymatrix)):
      if rows_with_zero[i]:
        nullify_row(mymatrix, i)
    for j in range(len(mymatrix[0])):
      if cols_with_zero[j]:
        nullify_col(mymatrix, j)
    return mymatrix

def nullify_row(mymatrix, row):
  for j in range(len(mymatrix[row])):
    mymatrix[row][j] = 0

def nullify_col(mymatrix, col):
  for i in range(len(mymatrix)):
    mymatrix[i][col] = 0

mymatrix = [[1,2,3], [4,0,6], [7,8,9]]
res = zeroMatrix(mymatrix)
print(res)
