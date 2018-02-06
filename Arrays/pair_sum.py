# Check for pair sum in array

def check(arr,x):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j]==x):
                print("Set "+ str(arr[i]) + ' ' + str(arr[j]))

arr = [1, 4, 45, 6, 10, -8]
check(arr,16)

