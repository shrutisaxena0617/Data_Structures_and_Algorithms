def reverseInteger(num):
  if num:
    sign = 1 if num > 0 else -1
    num_str = str(num)[:] if sign == 1 else str(num)[1:]
    mystack = []
    res = []
    for i in range(len(num_str)):
      # if num_str[i] == 0: # Don't need this as int() on ln 15 will remove any leading zeroes in string
      #   continue
      mystack.append(num_str[i])
    #print(mystack)
    while mystack:
      res.append(mystack.pop())
    #print(res)
    final = int(''.join(map(str, res)))
    #print(final)
    return 0 if (final >= pow(2,31) - 1) or (final <= pow(2,-31)) else sign * final
  else:
    return 0
    
# print(reverseInteger(-123456789780000))
print(reverseInteger(-123405670))
