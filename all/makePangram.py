class Solution:
  def makePangram(self, mystr):
    if mystr:
      char_array = [0]*256
      res = []
      for i in mystr:
        char_array[ord(i.lower())] = 1
      for j in range(97, 123):
        if char_array[j] != 1:
          res.append(chr(j))
      return res
    return 'Invalid input!!'

sol = Solution()
res = sol.makePangram('shruti')
print(res)
