def cost(arr):
    m, n = len(arr), len(arr[0])
    i = 1
    while i < m:
        a = arr[i - 1][:]
        min1 = a.index(min(a))
        a[min1] = float('inf')
        min2 = a.index(min(a))
        a = arr[i - 1]
        for j in range(n):
            if j == min1:
                arr[i][j] += a[min2]
            else:
                arr[i][j] += a[min1]
        i += 1
    return min(arr[-1])

print(cost([[1,2,3],[1,2,3],[3,3,1]]))