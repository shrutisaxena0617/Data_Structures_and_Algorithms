class Solution:
  def medianSortedArrays(self, arr1, arr2):
    if arr1 and arr2:
      while len(arr1) > 2:
          m1 = self.findMedian(arr1)
          m2 = self.findMedian(arr2)
          if m1 == m2:
            return m1
          elif m1 > m2:
            arr1 = [i for i in arr1 if arr[]]
            arr2 = arr2[m2:]
          else:
            arr1 = arr1[m1:]
            arr2 = arr2[0:m2]
      return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2
    elif arr1:
      return self.findMedian(arr1)
    elif arr2:
      return self.findMedian(arr2)
    else:
      return -1

  def findMedian(self, arr):
    if len(arr) %2 == 0:
      return (arr[int(len(arr)/2)-1] + arr[int(len(arr)/2)])/2
    else:
      return arr[int(len(arr)/2)]

sol = Solution()
res = sol.medianSortedArrays([1, 12, 15, 26, 38], [2, 13, 17, 30, 45])
print(res)
