class Solution:
  def squareElements(self, arr):
    return [x**2 for x in arr]

sol = Solution()
res = sol.squareElements([1,2,3])
print(res)
