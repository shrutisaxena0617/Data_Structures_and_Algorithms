class Solution:
  def find_factorial(self, num):
    if num>=0:
        fact = 1
        while num>0:
          fact *= num
          num -= 1
        return fact
    return -1

sol = Solution()
res = sol.find_factorial(3)
print(res)
#5*4*3*2*1
