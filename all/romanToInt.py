class Solution:
  def romanToInt(self, s):
    mydict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
    i = 0
    total = 0
    while i < len(s):
      if i+1 < len(s):
        try:
          total += mydict[s[i:i+2]]
          i += 2
        except:
          total += mydict[s[i]]
          i += 1
      else:
        total += mydict[s[i]]
        i += 1
    return total

sol = Solution()
res = sol.romanToInt('VIII')
print(res)
