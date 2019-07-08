class Solution:
  def findMajorityElement(self, arr):
    mydict = {}
    for k,v in enumerate(arr):
      mydict[v] = mydict.get(v, 0) + 1
    max_val = max(mydict.values())
    for k in mydict:
      if mydict[k] == max_val:
        return k

sol = Solution()
res = sol.findMajorityElement([1,1,1,2,4,5,6,1,1])
print(res)
