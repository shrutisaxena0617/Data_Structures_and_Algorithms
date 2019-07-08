def selectionSort(arr):
  if arr:
    for i in range(len(arr)):
      min = i
      for j in range(i+1, len(arr)):
        if arr[j] < arr[min]:
          min = j
      arr[i], arr[min] = arr[min], arr[i]
      print(arr)
    return arr
  return 'Invalid input!'

print(selectionSort([4,3,1,2]))
