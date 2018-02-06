# Array implementation in python (unsorted array) using in-built functions

# Function to insert element in an array
def insert(arr, elem):
    arr.append(elem)

# Function to delete element from array
def delete(arr, elem):
    arr.remove(elem)

# Function to search element in an array (Linear Search)
def search(arr, elem):
    for i in range(len(arr)):
        if(arr[i]==elem):
            print i
            return i
    print i
    return -1

# Function to display elements of an array
def display(arr):
    for i in range(len(arr)):
        print(arr[i])

# Creating an array
arr = []
print('Enter array elements followed by Enter key :: ')
empty_list = raw_input()
empty_list = empty_list.split()
for i in range(len(empty_list)):
    insert(arr, int(empty_list[i]))

# Display newly created array
display(arr)

# Search a key in the newly created array
index = search(arr, 20)
if(index!=-1):
    print('Element found at position ' + str(index+1))
else:
    print('Element not found')

# Delete element from the array
print('Displaying array before deleting ' + str(20))
display(arr)
delete(arr, 20)
print('Displaying array after deleting ' + str(20))
display(arr)






