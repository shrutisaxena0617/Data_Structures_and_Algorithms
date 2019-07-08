class Solution:
  def check_pair_sum(self, arr, target):
    if arr and target:
        mydict = {}
        for i in range(len(arr)):
          if (target - arr[i]) in mydict:
            return [mydict[target - arr[i]], i]
          else:
            mydict[arr[i]] = i
    return -1

sol = Solution()
res = sol.check_pair_sum([1,2,3,3], 6)
print(res)

# what it was trisum?
