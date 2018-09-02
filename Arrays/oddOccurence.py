class Solution:
  def oddOccurence(self, arr):
    mydict = {}
    res = []
    for k, v in enumerate(arr):
      mydict[v] = mydict.get(v, 0) + 1
    for k in mydict:
      if mydict[k] %2 != 0:
        res.append(k)
    return res

sol = Solution()
res = sol.oddOccurence([1,1,2,3,4,4,4,5,6,6])
print(res)
