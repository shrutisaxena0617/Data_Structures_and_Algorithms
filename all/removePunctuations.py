def removePunctuations(mystr):
  if mystr:
    res = []
    for i in mystr:
      if i.isalnum():
        res.append(i)
    return ''.join(res)
  return 'Invalid input!'

res = removePunctuations('Hello, shruti!!') #('Helloshruti')
# res = removePunctuations('') #('Invalid input!')
# res = removePunctuations(None) #('Invalid input!')
# res = removePunctuations('!!') # ('')
print(res)
