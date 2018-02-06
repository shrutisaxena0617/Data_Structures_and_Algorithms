# Factorial program using recursion

def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

print ('Enter number to compute factorial :: ')
user_input = int(raw_input())
fact = factorial(user_input)
print ('Factorial of ' + str(user_input) + ' is ' + str(fact))