def sol(s):
    if s:
        mydict = {}
        start, max_length = 0, 0
        for i in range(len(s)):
            if s[i] in mydict and start <= mydict[s[i]]:
                start = mydict[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            mydict[s[i]] = i
        return max_length
    else:
        return 0

print(sol('abcabcbb'))


def longestPalindrome(self, s):
    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

# get the longest palindrome, l, r are the middle indexes
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]
