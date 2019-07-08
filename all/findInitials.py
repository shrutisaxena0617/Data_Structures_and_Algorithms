def findInitials(mystr):
  if mystr:
    res = mystr.split(' ')
    final = []
    for i in res:
      final.append(i[0].upper()+' ')
    return ''.join(final)
  return 'Invalid input!!'

res = findInitials('shruti saxena')
print(res)
