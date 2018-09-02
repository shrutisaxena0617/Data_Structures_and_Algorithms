class Solution:
  def findMissingNumber(self, arr):
    if arr:
      size = len(arr) + 1
      sum_list = int((size * (size + 1)) / 2)
      return sum_list - sum(arr)
    return -1

sol = Solution()
res = sol.findMissingNumber([1, 2, 4, 6, 3, 7, 8])
print(res)
