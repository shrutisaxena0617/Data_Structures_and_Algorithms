def moveZeroes(nums):
  if nums:
    pos = 0
    for i in range(len(nums)):
      if(nums[i]):
        nums[pos], nums[i] = nums[i], nums[pos]
        pos += 1
    return nums

print(moveZeroes([1,2,3,4,0,6,7,0,4,0]))
