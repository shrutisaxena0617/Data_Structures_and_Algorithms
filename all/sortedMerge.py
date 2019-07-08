def sortedMerge(arr1, arr2):
  if arr1 and arr2:
    for i in range(len(arr1)-1, -1, -1):
     if arr1[i]:
      break # i = 4
    j = len(arr2)-1 # j =  3
    k = len(arr1)-1 # k = 8
    while i >=  0 and j >= 0 and k > 0:
      if arr1[i] >= arr2[j]:
        arr1[k] = arr1[i]
        i -= 1
      else:
        arr1[k] = arr2[j]
        j -= 1
      k -= 1
    return arr1

arr1 = [1,2,3,4,5,None,None,None,None]
arr2 = [10,20,30,40]
final = sortedMerge(arr1, arr2)
print(final)
