class Solution:
  def checkAnagram(self, mystr1, mystr2):
    if mystr1 and mystr2:
      num_chars = 256
      mystr1_count, mystr2_count = [0]*num_chars, [0]*num_chars
      for i in mystr1:
        mystr1_count[ord(i)] += 1
      for i in mystr2:
        mystr2_count[ord(i)] += 1
      for i in range(num_chars):
        if mystr1_count[i] != mystr2_count[i]:
          return False
      return True
    return False

sol = Solution()
res = sol.checkAnagram('hel', 'lekh')
print(res)
