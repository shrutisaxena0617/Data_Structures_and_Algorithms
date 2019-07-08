def sol(flowerbed, n):
    if flowerbed:
        new_flower_cnt = 0
        if len(flowerbed) > 1:
            if flowerbed[0] == flowerbed[1] == 0:
                flowerbed[0] = 1
                new_flower_cnt += 1
            if flowerbed[-1] == flowerbed[-2] == 0:
                flowerbed[-1] = 1
                new_flower_cnt += 1
            for i in range(1, len(flowerbed)-1):
                if flowerbed[i] == 1:
                    continue
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    new_flower_cnt += 1
                    flowerbed[i] = 1
            if n <= new_flower_cnt:
                return True
            else:
                return False
        else:
            if flowerbed[0] == 0 and n <= 1:
                return True
            elif flowerbed[0] == 1 and n == 0:
                return True
            else:
                return False

print(sol([1], 0))
