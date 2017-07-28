def findoperations(hill,n,m,l):
    ans = 0
    a = n - 1
    b = n+m - 1
    c = n + 2*m -1 - 1
    for i in range(0,a+1):
        ans += hill[i]
    stepsize = 1
    for i in range(a+1,b+1):
        ans += (hill[i] - stepsize)
        if(stepsize > hill[i]):
            return float('inf')
        stepsize += 1
    stepsize -= 2
    for i in range(b+1,c+1):
        ans += (hill[i] - stepsize)
        if(stepsize > hill[i]):
            return float('inf')
        stepsize -= 1
    for i in range(c+1,len(hill)):
        ans += hill[i]
    return ans



t = int(input())
for test in range(t):
    hill_len = int(input())
    hill = list(map(int,input().split(' ')))
    n = 0
    m = 1
    l = 0
    print(findoperations(hill,n,m,l))
