import heapq
class Solution: #priority queue
  # def sortElemsByFrequency(self, arr):
  #   if arr:
  #     mydict = {}
  #     for k,v in enumerate(arr):
  #       mydict[v] = mydict.get(v, 0) + 1
  #     sorted_dict = sorted(mydict.items(), key = lambda x:x[1])
  #     return sorted_dict

      def sortElemsByFrequency(self, arr):
        if arr:
          x = []
          res = []
          mydict = {}
          for k,v in enumerate(arr):
            mydict[v] = mydict.get(v, 0) + 1
          for k,v in mydict.items():
              heapq.heappush(x, (v,k))
          while x:
              res.insert(0, heapq.heappop(x)[1])
          return res

sol = Solution()
res = sol.sortElemsByFrequency([2, 5, 2, 8, 5, 6, 8, 8])
print(res)
