# Check the solution and how will you print the subarray
class Solution:
  def findmaxContinuousSubArray(self, arr):
    #Kadene's algorithm
    if arr:
      max_end_here, max_so_far = arr[0], arr[0]
      for i in range(len(arr)):
        if max_end_here + arr[i] > max_end_here:
          max_end_here += arr[i]
        if max_end_here > max_so_far:
          max_so_far = max_end_here
      return max_so_far
    return -1

sol = Solution()
# res = sol.findmaxContinuousSubArray([-2, -3, 4, -1, -2, 1, 5, -3])
res = sol.findmaxContinuousSubArray([-2, -3, -4, -1, -2, -1, -5, -3])
print(res)
