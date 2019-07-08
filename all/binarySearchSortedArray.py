def search(nums, target):
    if nums:
        pivot = -1
        res = -1
        if len(nums) > 1:
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    pivot = i
                    break
            #print(pivot)
            if pivot == -1:
                res = binarysearch(nums, target, 0, len(nums)-1)
            elif target >= nums[0]:
                res = binarysearch(nums, target, 0, pivot)
            else:
                res = binarysearch(nums, target, pivot+1, len(nums)-1)
            if res is not None:
                return res
            else:
                return -1
        elif nums[0] == target:
            return 0
    return -1

def binarysearch(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        #print(mid)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

print(search([1,3],1))

# edge cases -> no pivot, array length < 2, element not found 
