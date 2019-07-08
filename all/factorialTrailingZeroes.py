def sol(n):
  if n == 0:
    return 0
  return n//5 + sol(n//5)

print(sol(10))
