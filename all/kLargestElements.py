import heapq
class Solution:
  # def kLargestElements(self, arr, k):
  #   arr.sort(reverse = True)
  #   for i in range(k):
  #     print(arr[i])

  def kLargestElements(self, arr, k):
    heapq.heapify(arr)
    print(heapq.nlargest(k, arr))

sol = Solution()
sol.kLargestElements([1, 23, 12, 9, 30, 2, 50], 3)

#implement priority queue
