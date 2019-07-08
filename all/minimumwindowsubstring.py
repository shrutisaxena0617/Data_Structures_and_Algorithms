def sol(s, t):
    if str:
        need = {}
        missing = len(t)
        for k,v in enumerate(s):
            need[v] = need.get(v, 0) + 1
        left, min_left, min_len = 0, 0, len(s) + 1
        for right, char in enumerate(s):
            if char in need:
                need[char] -= 1
                if need[char] >= 0:
                    missing -= 1
            while missing == 0:
                if right - left + 1 < min_len:
                    min_left = left
                    min_len = right - left + 1
                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        missing += 1
                left += 1
        if min_len > len(s):
            return ''
        return s[min_left:min_left + min_len]

print(sol('shruti', 'sig'))
