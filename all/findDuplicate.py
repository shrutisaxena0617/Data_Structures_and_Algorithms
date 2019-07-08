class Solution:
  def findDuplicate(self, arr):
    mydict = {}
    for k,v in enumerate(arr):
      mydict[v] = mydict.get(v, 0) + 1
    return mydict.keys()

sol = Solution()
res = sol.findDuplicate([1,2,2,3,3,3,4,5])
print(res)
