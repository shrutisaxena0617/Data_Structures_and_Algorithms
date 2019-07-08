# class Solution:
#   def bestTimeToBuySellStock(self, arr):
#     if arr:
#       minBuy = float('inf')
#       maxProfit = 0
#       res = []
#       for i in arr:
#         maxProfit = max(maxProfit, i-minBuy)
#         minBuy = min(i, minBuy)
#         if maxProfit > 0:
#             res.append(maxProfit)
#             minBuy = float('inf')
#             maxProfit = 0
#       return res
#     else:
#       return -1
#
# sol = Solution()
# res = sol.bestTimeToBuySellStock([1,2,3,4,5])
# print(res)

def bestTimeToBuySellStock(prices):
    if prices:
        min_price = float('INF')
        sum_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            if price - min_price > 0:
                sum_profit += price - min_price
                min_price = price
        return sum_profit

print(bestTimeToBuySellStock([1,2,3,4,5,5,6,4,7,8,9]))
