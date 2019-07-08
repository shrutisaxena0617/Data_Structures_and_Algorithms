# def findExtraCharacter(mystr1, mystr2): #can do with xor as well
#   if mystr1 and mystr2:
#     larger_str = mystr1 if len(mystr1) > len(mystr2) else mystr2
#     smaller_str = mystr1 if len(mystr1) < len(mystr2) else mystr2
#     char_array = [0]*256
#     for i in smaller_str:
#       char_array[ord(i)] = 1
#     for j in larger_str:
#       if char_array[ord(j)] != 1:
#         return j
#   return 'Invalid input!!'
#
# res = findExtraCharacter('shhuti', 'shuti') # Throws 'Invalid input'
# print(res)

# May not work if characters are not in order. In that case, first sort
def findExtraCharacter(mystr1, mystr2): #can do with xor as well
  if mystr1 and mystr2:
    larger_str = mystr1 if len(mystr1) > len(mystr2) else mystr2
    smaller_str = mystr1 if len(mystr1) < len(mystr2) else mystr2
    for i in range(len(smaller_str)):
      if larger_str[i] != smaller_str[i]:
        return larger_str[i]
    return larger_str[i+1]
  return 'Invalid input!!'

res = findExtraCharacter('shutii', 'shuti')
print(res)
