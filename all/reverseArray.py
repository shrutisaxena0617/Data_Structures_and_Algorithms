class Solution:
    def reverseArray(self, arr):
        if arr:
            j = len(arr)-1
            for i in range(0, int(len(arr)/2)):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                j = j-1
            return arr
        else:
            return -1

sol = Solution()
res = sol.reverseArray([1,2,3,4,5])
print(res)
