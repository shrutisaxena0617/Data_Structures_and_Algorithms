# def leftSubArrayLessThanRight(arr):
#   if arr:
#     i = 0
#     res_len = 0
#     while i < len(arr)-1:
#       left_max = max(arr[:i+1])
#       res_len = i + 1
#       right_min = min(arr[i+1:])
#       if left_max <= right_min:
#           break
#       else:
#           i += 1
#     return res_len
#   return 'Invalid Input!'

def leftSubArrayLessThanRight(arr): # more concise code
    if arr:
        res_len = 0
        for i in range(len(arr)):
          if max(arr[:i+1]) > min(arr[i+1:]):
              return i+1
    return 'Invalid Input!'

print(leftSubArrayLessThanRight([1,0,3,8,6]))
