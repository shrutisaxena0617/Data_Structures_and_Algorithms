def stringCompression(mystr):
  if mystr:
    res = []
    mydict = {}
    for i in mystr:
      mydict[i] = mydict.get(i, 0) + 1
    i = 0
    while i < len(mystr):
      res.append(mystr[i])
      res.append(mydict[mystr[i]])
      i += mydict[mystr[i]]
    return ''.join(map(str, res)) #if len(res) < len(mystr) else mystr
  return 'Invalid input'

#res = stringCompression('aabbbbcccdd')
res = stringCompression('abbc')
print(res)

# a:2, b:4, c:3, d:2
# [a]
