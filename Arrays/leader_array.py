# Find leaders in an array
# An element is leader if it is greater than all the elements to its right side

def find_leader(arr):
    leader = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]<=arr[j]):
                flag = 0
                break
            else:
                flag = 1
            if(i==len(arr)-1):
                flag = 1
        if(flag==1):
            leader.append(arr[i])
    return leader

def display(arr):
    for i in range(len(arr)):
        print arr[i]

arr = [16, 17, 4, 3, 5, 2]
#arr = [10,10,10,10,20] ##### not working check this!!
print('Displaying original array')
display(arr)
print('Displaying leaders')
leader = find_leader(arr)
display(leader)