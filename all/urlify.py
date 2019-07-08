def urlify(mystr1, true_len):
    if mystr1:
        space_cnt = 0
        mystr = list(mystr1)
        for i in range(true_len):
            if mystr[i] == ' ':
                space_cnt += 1
        #print(space_cnt)
        index = true_len + space_cnt * 2
        #print(index)
        if true_len < len(mystr):
            mystr[true_len] = '\0'
        for i in range(true_len-1, -1, -1):
            if mystr[i] == ' ':
                mystr[index-1] = '0'
                mystr[index-2] = '2'
                mystr[index-3] = '%'
                index -= 3
            else:
                mystr[index-1] = mystr[i]
                index -= 1
        return mystr
    return 'Invalid input!!'
 # def urlify(mystr):
 #   res = []
 #   stripped = mystr.strip()
 #   for i in range(len(stripped)):
 #     if stripped[i] == ' ':
 #       res.append('%20')
 #     else:
 #       res.append(stripped[i])
 #   return ''.join(res)

res = urlify('hello shruti    ', 12)
print(res)
