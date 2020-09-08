#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/speed-7/
t=(int(input()))
for i in range(t):
    n=(int(input()))
    li=list(map(int, input().split()))
    smallest=li[0]
    count=1
    for j in range(1,n):
        if li[j]<=smallest:
            count+=1
            smallest=li[j]
    print(count)
    del li[:]
