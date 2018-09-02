class Solution:
  # def checkOddOccurence(self, arr):
  #     if arr:
  #       mydict = {}
  #       res = []
  #       for k,v in enumerate(arr):
  #         mydict[v] = mydict.get(v, 0) + 1
  #       for k,v in mydict.items():
  #         if v%2 != 0:
  #           res.append(k)
  #       return res
  #     return -1
 def checkOddOccurence(self, arr): # great solution with S(1) and O(n) if all elements in list are duplicate except one
    if arr:
        res = 0
        for i in arr:
            res = res ^ i
        return res
    return -1

sol = Solution()
res = sol.checkOddOccurence([1,1,1,2,3,4,5,6,6])
print(res)
