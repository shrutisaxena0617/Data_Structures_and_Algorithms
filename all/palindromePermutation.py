def palindromePermutation(mystr):
  if mystr:
    char_array = [0]*128
    for i in mystr:
      char_array[ord(i)] += 1
    odd_count = 0
    for j in char_array:
      if j % 2 != 0:
        if odd_count > 0:
          return False
        else:
          odd_count += 1
    return True
  return 'Invalid input!!'

res = palindromePermutation('ssii')
print(res)
