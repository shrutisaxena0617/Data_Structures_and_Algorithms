def sol(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n < 0:
        return sol(1/x, -n)
    else:
        if n%2 == 0:
            return sol(x*x, n/2)
        else:
            return sol(x*x, (n-1)/2) * x

print(sol(2,-3))
