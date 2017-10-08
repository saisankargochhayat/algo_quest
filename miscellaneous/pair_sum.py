#Find Pair of Numbers in Array with a Given Sum
from collections import defaultdict
arr=list(map(int, input().split(' ')))
s=int(input())
d=defaultdict(int)
for i in arr:
    d[i]+=1
print(list(d.keys()))
for i in list(d.keys()):
    n=s-i
    if i==n:
        if d[i]>1:
            print(i,n)
            d[i]-=1
    elif i!=n:
        if d[n]!=0:
            print(i,n)

# output
# 1 2 3 4 5 5 6 7
# 10
# [1, 2, 3, 4, 5, 6, 7]
# 3 7
# 4 6
# 5 5
# 6 4
# 7 3
