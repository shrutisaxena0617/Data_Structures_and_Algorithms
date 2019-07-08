def TripleStep(n, memo):
  if n<0:
    return 0
  if n==0:
    return 1
  if memo[n] is None:
    memo[n] = TripleStep(n-1, memo) + TripleStep(n-2, memo) + TripleStep(n-3, memo)
    print(memo)
  return memo[n]

n = 5
memo = [None]*(n+1)
print(TripleStep(n, memo))
