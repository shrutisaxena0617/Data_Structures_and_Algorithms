def stringRotation(mystr1, mystr2):
  if mystr1 and mystr2:
    if len(mystr1) != len(mystr2):
      return False
    mystr1_new = mystr1 * 2
    if mystr2 in mystr1_new:
      return True
    else:
      return False
  return 'Invalid input!'

res = stringRotation('shruti', 'rutish')
print(res)
