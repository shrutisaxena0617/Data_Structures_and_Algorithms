def isUnique(mystr):
  if mystr:
    char_array = [0]*256
    for i in mystr:
      if char_array[ord(i)] == 1:
        return False
      else:
        char_array[ord(i)] = 1
    return True
  return 'Invalid input'

res = isUnique('shrutii')
print(res)
