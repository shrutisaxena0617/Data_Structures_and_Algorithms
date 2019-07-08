def checkPermutationString(mystr1, mystr2):
  if mystr1 and mystr2:
    if len(mystr1) != len(mystr2):
      return False
    char_array1, char_array2 = [0]*128, [0]*128
    for i in mystr1:
      char_array1[ord(i)] += 1
    for i in mystr2:
      char_array2[ord(i)] += 1
    for i in range(97, 123):
      if char_array1[i] != char_array2[i]:
        return False
    return True
  return 'Invalid input'

# res = checkPermutationString('sssiii', 'iiiiss')
res = checkPermutationString('shruti', 'itursh')
print(res)
