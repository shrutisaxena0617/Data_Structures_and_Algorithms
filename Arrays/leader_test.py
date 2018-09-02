import numpy as np
class Solution:
  def findLeader(self, arr):
    if arr:
      leaders = []
      max_from_right = np.NINF
      for i in range(len(arr)-1, -1, -1):
        if i == len(arr)-1 or arr[i] > max_from_right:
          max_from_right = arr[i]
          leaders.append(max_from_right)
      return leaders

sol = Solution()
leaders = sol.findLeader([16, 17, 4, 3, 5, 2])
print(leaders)
