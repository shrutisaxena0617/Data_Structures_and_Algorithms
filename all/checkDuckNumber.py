def checkDuckNumber(num):
  return 'Not duck' if str(num)[0] == 0 else 'Duck'

res = checkDuckNumber(123)
print(res)
