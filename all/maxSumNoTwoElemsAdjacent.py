class Solution:
  def maxSumNoTwoElemsAdjacent(self, arr):
    if arr:
      inc, exc = 0, 0
      for i in arr:
        new_exc = exc if exc > inc else inc
        inc = exc + i
        exc = new_exc
      return exc if exc > inc else inc

sol = Solution()
#res = sol.maxSumNoTwoElemsAdjacent([5, 5, 10, 100, 10, 5]) #110
res = sol.maxSumNoTwoElemsAdjacent([5, 5, 10, -100, 10, 5]) #25
print(res)
