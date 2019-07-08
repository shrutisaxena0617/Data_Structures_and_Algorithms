def searchRange(nums, target):
    res = [-1,-1]
    if nums:
        return searchRangeHelp(nums, target, 0, len(nums)-1)
    return res

def searchRangeHelp(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid] and target == nums[mid-1]:
            return [mid-1, mid]
        elif target == nums[mid] and target == nums[mid+1]:
            return [mid, mid+1]
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

print(searchRange([5,7,7,8,8,10], 8))
