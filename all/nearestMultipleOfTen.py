def nearestMultipleOfTen(num):
  if num == 0:
    return num
  else:
    smaller_multiple = (num // 10) * 10
    larger_multiple = smaller_multiple + 10
  return smaller_multiple if (num - smaller_multiple) < (larger_multiple - num) else larger_multiple

res =  nearestMultipleOfTen(2564)
print(res)
