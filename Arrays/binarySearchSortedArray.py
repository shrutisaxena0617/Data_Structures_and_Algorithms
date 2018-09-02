class Solution:
  def binarySearchArray(self, arr, elem):
    if arr:
      return self.binarySearchArrayHelp(0, (len(arr)-1), arr, elem)
    return -1
  def binarySearchArrayHelp(self, l, r, arr, elem):
    while l <= r:
        mid = int(l + (r - l)/2)
        if arr[mid] == elem:
            return mid
        elif arr[mid] < elem:
            l = mid + 1
        else:
            r = mid - 1
    return -1

sol = Solution()
res = sol.binarySearchArray([1,2,3,4,5,6,7,8,9,10], 4)
print(res)
