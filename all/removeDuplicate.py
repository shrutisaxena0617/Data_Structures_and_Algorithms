# Leetcode easy
# Remove duplicates from sorted array
def removeDuplicate(nums):
  if nums:
    i = 0
    for num in nums:
        if i == 0 or num != nums[i - 1]:
            nums[i] = num
            i += 1
    return nums[:i]

print(removeDuplicate([1,1,2,2]))
# print(removeDuplicate([1,2,1,2])) # This will not work so first sort
