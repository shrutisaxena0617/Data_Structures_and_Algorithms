# BT

# binarysearchtree
#binarytree
#BFSBT
#checkbalancedtree
#checkbst
#connectnodesllbt
#issymmetricBT
#ksumpathsBT
#findlowestcommonancestor
#find random node

# LL

# checkPalindromeLL
# circularlinkedlistimplementation
#deletemiddleLL
#doublyLL
#findintersectionnodell
#levelLL
#linkedlistimpl
#linkedlistpartition
LLremoveduplicate

#findislands
#fibonacci - do this extensively

def sol(flowerbed, n):
    if flowerbed:
        if len(flowerbed) > 1:
            new_flower_cnt = 0
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                new_flower_cnt += 1
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] = 1
                new_flower_cnt += 1
            for i in range(1, len(flowerbed)-1):
                if flowerbed[i] == 1:
                    continue
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    new_flower_cnt += 1
            if n <= new_flower_cnt:
                return True
            return False
        elif len(flowerbed) == 1 and flowerbed[0] == 1 and n == 0:
            return True
        elif len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        else:
            return False

print(sol([1,0,0,0,1], -1))
