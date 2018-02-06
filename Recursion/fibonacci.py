# Program for fibonacci using recursion

#def fibonacci(n):
#    if(n==0):
#        return 0
#    elif(n==1):
#        return 1
#    else:
#        print n, fibonacci(n-2) + fibonacci(n-1)
#        return fibonacci(n-2) + fibonacci(n-1)

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return n + fibonacci(n-1)

print ('Enter the number for fibonacci :: ')
user_input = int(raw_input())
result = fibonacci(user_input)
print ('Fibonacci result for ' + str(user_input) + ' is ' + str(result))
