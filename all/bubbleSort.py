def bubbleSort(arr):
  if arr:
    if len(arr) <= 1:
      return arr
    for i in range(len(arr)-1):
      for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
          arr[i], arr[j] = arr[j], arr[i]
    return arr
  return 'Invalid input!'

print(bubbleSort([2,3,6,3,8,1,-1]))
