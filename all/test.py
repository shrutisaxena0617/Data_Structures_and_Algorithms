# def fetchItemsToDisplay(items, sortParameter, sortOrder, itemPerPage, pageNumber):
#     if not items:
#         return
#
#     if sortParameter > len(items):
#         return
#
#     if sortOrder != 0 and sortOrder !=1:
#         return
#
#     if itemPerPage < 0:
#         return
#
#     if pageNumber < 0:
#         return
#
#     li = list(sorted(items, key = lambda item: item[sortParameter], reverse = sortOrder == 1))
#     print(li)
#
#     start = (pageNumber) * itemPerPage
#     end = start + itemPerPage
#     print(start, end)
#
#     return [i[0] for i in li[start:end]]
#
# items = [('owjevtkuyv', 58584272, 62930912), ('rpaqgbjxik', 9425650, 96088250), ('dfbkasyqcn', 37469674, 46363902), ('vjrrisdfxe', 18666489, 88046739)]
# res = fetchItemsToDisplay(items, 2,1,2,0)
# print('result is ', res)

# Landing AI
# a = 2437
# b = 875
# x = a
# y = b
# while x!=y:
#     if x>y:
#         x = x-y
#     if x<y:
#         y = y-x
# print(x)


# # # # # def op(x):
# # # # #     if x%3 == 1:
# # # # #         return x%3
# # # # #     else:
# # # # #         return x + op(x-1)
# # # # #
# # # # # print(op(316))
# # # #
# # # #
# # # # def overlapping(lista, listb):
# # # #     out = [i for i in lista if i in listb]
# # # #     return out
# # # #
# # # # print(overlapping([1,2,3], [2,3,4]))
# # #
# # # def f(x):
# # #     x /= 2
# # #     return x+3
# # # def g(x,y):
# # #     x *= y+2
# # #     return x
# # # def h(x,y):
# # #     return x*y
# # # out = g(f(4), h(3,2))
# # # print(out)
# #
# #
# # def divisors(num):
# #     list_div = []
# #     for i in range(1, num):
# #         if num%i == 0:
# #             list_div.append(i)
# #     return list_div
# #
# # print(divisors(12))
#
# A = '____'.join([' ', ' ', ' ', ' ', ' '])
# #B = ''.join(['|','|','|','|','|'])
# B = '||||'.join(['-','-','-','-'])
# print('\n'.join((A,B,A,B,A,B,A,B,A)))

def func(num):
    return [i for i in num if i%3 == 0]

print(func([1,2,3,4,5,6]))
