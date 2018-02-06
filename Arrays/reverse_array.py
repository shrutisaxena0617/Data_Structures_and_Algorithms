# Reverse an unsorted array

# Function to insert elements into array
def insert(arr, elem):
    arr.append(elem)

# Function to reverse the array

def reverse(arr):
    n = len(arr)
    for i in range(n/2):
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp
    return arr

def display(arr):
    for i in range(len(arr)):
        print arr[i]

arr = []
print('Enter array elements followed by Enter key :: ')
empty_list = raw_input()
empty_list = empty_list.split()
for i in range(len(empty_list)):
    insert(arr,int(empty_list[i]))
print ('Displaying array before reversing')
display(arr)
arr_reverse = reverse(arr)
print ('Displaying array after reversing')
display(arr_reverse)



