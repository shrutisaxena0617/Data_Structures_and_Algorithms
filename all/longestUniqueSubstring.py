def longestUniqueSubstring(mystr):
  if mystr:
    i = 0
    j = 0
    max_len = 0
    myset = set()
    while i < len(mystr) and j < len(mystr):
        if ord(mystr[j]) not in myset:
            myset.add(ord(mystr[j]))
            j += 1
            max_len = max(max_len, j-i)
        else:
            myset.remove(ord(mystr[i]))
            i+=1
    return max_len

print(longestUniqueSubstring('asdhsflsdhfd'))
