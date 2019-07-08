class Solution: #O(n), S(d)
    # def arrRotation(self, arr, d):
    #     if arr and d:
    #         temp = []
    #         for i in range(len(arr)-d):
    #             if i<d:
    #                 temp.append(arr[i])
    #             arr[i] = arr[i+d]
    #         for i in range(d):
    #             #print(len(arr)-d+i)
    #             arr[len(arr)-d+i] = temp[i]
    #         return arr
    #     return -1

    # def arrRotation(self, arr, d): # leftrotate
    #     temp = arr[:d]
    #     for i in range(len(arr) - d):
    #         arr[i] = arr[i+d]
    #     for i in range(d):
    #         arr[len(arr)-d+i] = temp[i]
    #     return arr
    def arrRotation(self, arr, d): # rightrotate
        temp = arr[-d:]
        for i in range(len(arr)-1, d-1, -1):
            arr[i] = arr[i-d]
        arr[:d] = temp
        return arr

sol = Solution()
res = sol.arrRotation([1,2,3,4,5], 3) # [3,4,5,1,2]
print(res)

# class Solution: #O(n*d), S(1)
#   def arrayRotate(self, arr, d):
#     if arr and d:
#       for i in range(d):
#         self.arrayRotateByOne(arr, d)
#       return arr
#     else:
#       return -1
#   def arrayRotateByOne(self, arr, d):
#     temp = arr[0]
#     for i in range(len(arr) - 1):
#       arr[i] = arr[i+1] #shift left
#     arr[len(arr) - 1] = temp
#
# sol = Solution()
# res = sol.arrayRotate([1,2,3,4,5,6], 2) # Handle negative rotation
# print(res)


# def rotate(nums, k):
#     k = k % len(nums)
#     nums[:] = nums[-k:] + nums[:-k]
#     return nums
