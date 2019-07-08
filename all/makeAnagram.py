class Solution:
  def makeAnagram(self, mystr1, mystr2):
    if mystr1 and mystr2:
      # num_chars = 256
      # mystr1_count, mystr2_count = [0]*num_chars, [0]*num_chars
      # for i in mystr1:
      #   mystr1_count[ord(i)] += 1
      # for i in mystr2:
      #   mystr2_count[ord(i)] += 1
      if len(mystr1) == len(mystr2):
          # replacement
          unequal_count = 0
          for i in range(len(mystr1)):
              if mystr1[i] != mystr2[i]:
                  if unequal_count >= 1:
                      return 'More than one edit'
                  unequal_count += 1
          return 'Replacement with one edit'
      elif abs(len(mystr1) - len(mystr2)) == 1:
          # insertion or deletion
          unequal_count = 0
          i, j = 0, 0
          while i < len(mystr1) and j < len(mystr2):
              if mystr1[i] != mystr2[j]:
                  if unequal_count >= 1:
                      return 'More than one edit'
                  unequal_count += 1
                  if i<len(mystr1)-1:
                      if mystr1[i+1] == mystr2[j]:
                          i+=1
                  elif j<len(mystr2)-1:
                      if mystr1[i] == mystr2[j+1]:
                          j+=1
                  else:
                      return 'More than one edit'
              else:
                  i+=1
                  j+=1
          return 'Insertion or deletion with one edit'
      return 'More than one edit'
    return 'Invalid input'

sol = Solution()
res = sol.makeAnagram('hell', 'hello')
print(res)
