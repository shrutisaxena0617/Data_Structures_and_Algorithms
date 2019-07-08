def sol(arr):
    if arr:
        p = 1
        output = []
        for i in arr:
            output.append(p)
            p *= i
        p = 1
        for i in range(len(arr)-1, -1, -1):
            output[i] *= p
            p *= arr[i]
        return output

print(sol([1,2,3,4,-5]))
