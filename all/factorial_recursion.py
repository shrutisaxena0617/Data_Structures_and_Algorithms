class Solution:
    def find_factorial(self, num):
        if num == 0:
            return 1
        elif num > 0:
            return num * self.find_factorial(num-1)
        else:
            return -1

sol = Solution()
res = sol.find_factorial(-1)
print(res)
