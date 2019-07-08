def checkAllCharsSame(mystr):
  if mystr:
    for i in range(1, len(mystr)):
      if mystr[i] != mystr[0]:
        return False
    return True
  return 'Invalid input!!'

res = checkAllCharsSame('hkh')
print(res)
