def sol(A, B):
    res = {}
    mydict = {}
    final_res = []
    for i in B:
        res_list = []
        for j in A:
            c = 0
            while c < len(i):
                if i[c] not in j:
                    break
                else:
                    c += 1
            if c == len(i):
                res_list.append(j)
        res[i] = res_list
    # final = [value for values in res.values() for value in values]
    final = []
    for k in list(res.values()):
        print(k)
        final.extend(k)
    print(final)
    for k, v in enumerate(final):
        mydict[v] = mydict.get(v, 0) + 1
    for k, v in mydict.items():
        if v >= len(B):
            final_res.append(k)
    return final_res

res = sol(["amazon","apple","facebook","google","leetcode"], ["lo","eo"])
print(res)
