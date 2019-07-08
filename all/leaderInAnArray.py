import numpy as np
class Solution:
  def findLeader(self, arr):
    leaders = []
    max_from_right = np.NINF
    for i in range(len(arr)-1, -1, -1):
      if i == len(arr)-1 or arr[i] > max_from_right:
        max_from_right = arr[i]
        leaders.append(max_from_right)
    return leaders

sol = Solution()
res = sol.findLeader([1,2,3,4,5,4])
print(res)

#[16, 17, 4, 3, 5, 2]
