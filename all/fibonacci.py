# def fib(): #iterator and generator
#     a, b = 1, 1
#     while True:
#         yield a
#         a, b = b, a+b
#
# for i, num in zip(range(5), fib()):
#     print(num)

# # using cache
# from functools import lru_cache
# @lru_cache(maxsize=1000)
# def fib(n): #recursion
#     if n <= 1:
#         return 1
#     else:
#         return fib(n-1) + fib (n-2)
#
# # for i in range(35): # very slow
# #     print(fib(i))
# print(fib(100))

# dynamic programming
def fib(n, memo):
    # if n == 1 or n == 0:
    #     return n
    if memo[n] is None:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        #print(memo)
    return memo[n]

n = 200
memo = [None]*(n+1)
memo[0] = 0
memo[1] = 1
print(fib(n, memo))
