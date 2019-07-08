# class Solution:
#     def longestCommonPrefix(self, strs):
#         if strs:
#             check = strs[0]
#             for i in range(len(strs)):
#                 res = []
#                 ex_len = len(check) if len(check) <= len(strs[i]) else len(strs[i])
#                 for j in range(ex_len):
#                     if check[j] == strs[i][j]:
#                         res.append(check[j])
#                     else:
#                         break
#                 check = res
#             return ''.join(res)
#         return ''
#
# sol = Solution()
# res = sol.longestCommonPrefix(['abc', 'abcdddd', 'abcd'])
# print(res)

def findLongestCommonPrefix(strings):
    if strings:
        min_len = float('INF')
        for i in range(len(strings)):
            min_len = min(len(strings[i]), min_len)
        low = 1
        high = min_len
        while low <= high:
            mid = (low+high) // 2
            if isCommonPrefix(strings, mid):
                low = mid + 1
            else:
                high = mid - 1
        return strings[0][:(low+high)//2]

def isCommonPrefix(strings, some_len):
    checkStrNew = strings[0][:some_len]
    for i in range(len(strings)):
        if strings[i][:some_len] != checkStrNew:
            return False
    return True

print(findLongestCommonPrefix(['abc', 'abcdddd', 'abcd']))
