class Solution:
  def checkPangram(self, mystr):
    if mystr:
      char_array = [0]*256
      for i in mystr:
        char_array[ord(i.lower())] = 1
      for i in range(97, 123):
          if char_array[i] == 0:
              return False
      return True
    return 'Invalid input!!'

sol = Solution()
res = sol.checkPangram('The quick brown fox jumps over the lazy dog')
print(res)
