class Solution:
  def mergeSortedArrays(self, arr1, arr2):
    if arr1 and arr2:
        final_arr = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                final_arr.append(arr1[i])
                i += 1
            else:
                final_arr.append(arr2[j])
                j += 1
        if i != len(arr1):
            final_arr.extend(arr1[i:])
        elif j != len(arr2):
            final_arr.extend(arr2[j:])
        return final_arr
    elif arr1:
        return arr1
    elif arr2:
        return arr2
    else:
        return -1

sol = Solution()
res = sol.mergeSortedArrays([1, 12, 15, 26, 38], [2, 13, 17, 30, 45])
print(res)
