# def magicIndex(arr):
#   if arr:
#     return magicIndexBinarySearch(arr, 0, len(arr)-1)
#
# def magicIndexBinarySearch(arr, l, r):
#   while l<r:
#     mid = (l+r)//2
#     if arr[mid] == mid:
#       return mid
#     elif arr[mid] > mid:
#       return False
#     elif arr[mid] < mid:
#       r = mid -1
#
# res = magicIndex([1,1,1,5,7])
# print(res)

def magicIndex(arr):
    if arr:
        return magicIndexBinarySearchRec(arr, 0, len(arr)-1)

def magicIndexBinarySearchRec(arr, l, r):
    if l > r:
        return
    mid = (l + r)//2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return magicIndexBinarySearchRec(arr, l, mid-1)
    elif arr[mid] < mid:
        return magicIndexBinarySearchRec(arr, mid+1, r)
    return False

res = magicIndex([1,1,2])
print(res)
