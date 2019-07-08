def sol(arr1, arr2):
  if arr1 and arr2:
    mydict = {}
    result = []
    for i in arr1:
      mydict[i] = mydict.get(i, 0) + 1
    for j in arr2:
      if j in mydict and mydict[j] > 0:
        result.append(j)
        mydict[j] -= 1
    return result

# print(sol([1,2,2,1], [2,2]))
print(sol([4,9,5], [9,4,9,8,4]))
