def plusOne(digits):
  if digits:
    digits_to_str = [str(i) for i in digits]
    digits_to_int = int(''.join(digits_to_str)) + 1
    mystr = str(digits_to_int)
    res = [int(i) for i in mystr]
    return res

print(plusOne([1,2,3]))
