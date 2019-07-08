def sol(num):
  if num == 0:
    return num
  left, right = 1, (num//2) + 1
  while True:
    mid = (left + right) // 2
    if mid*mid > num:
      right = mid - 1
    else:
      if (mid+1)*(mid+1) > num:
        return mid
      left = mid + 1

print(sol(25))
