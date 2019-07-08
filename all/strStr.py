def strStr(haystack, needle):
    if not needle:
        return 0
    if not haystack:
        return -1
    needle_len = len(needle)
    i = 0
    while i <= len(haystack) - needle_len:
        if haystack[i:i+needle_len] == needle:
            return i
        i+=1
    return -1

print(strStr('aasa', 'as'))
