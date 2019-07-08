class Solution:
  def searchSortedRotatedArray(self, arr, elem):
    if arr and elem:
      for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
          pivot = i
          break
      if elem == arr[i]:
        return i
      elif elem >= arr[0]:
        return self.binarySearch(0, pivot, arr, elem)
      else:
        return self.binarySearch(pivot, len(arr) - 1, arr, elem)
    return -1

  def binarySearch(self, l, r, arr, elem):
    while l<= r:
      mid = int(l + (r-1) / 2)
      if elem == arr[mid]:
        return mid
      elif elem < arr[mid]:
        r = mid - 1
      else:
        l = mid + 1
    return -1


sol = Solution()
res = sol.searchSortedRotatedArray([5, 6, 7, 8, 9, 10, 1, 2, 3], 9)
print(res)
