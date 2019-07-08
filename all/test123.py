def sol(c):
    # mylist = [x**2 for x in range(c+1)]
    # print(mylist)
    # left = 0
    # right = len(mylist) - 1
    # while left <= right:
    #     if mylist[left] + mylist[right] == c:
    #         return True
    #     elif mylist[left] + mylist[right] > c:
    #         right -= 1
    #     else:
    #         left += 1
    # return False
    #mylist = [x**2 for x in range(c+1)]
    #print(mylist)
    left = 0
    right = int(c**0.5)
    while left <= right:
        if left**2 + right**2 == c:
            return True
        elif left**2 + right**2 > c:
            right -= 1
        else:
            left += 1
    return False

print(sol(10000000))
