class Solution:
  def isPalindrome(self, mystr):
    if mystr:
        i = 0
        j = len(mystr)-1
        mystr = mystr.lower()
        while(i<=j):
            if not mystr[i].isalnum():
                i+=1
                continue
            if not mystr[j].isalnum():
                j-=1
                continue
            if mystr[i] != mystr[j]:
                return False
            i+=1
            j-=1
        return True
    return False

sol = Solution()
res = sol.isPalindrome('shruti  123321iturhs')
print(res)
