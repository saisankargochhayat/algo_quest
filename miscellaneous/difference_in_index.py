#https://www.hackerrank.com/contests/stryker-codesprint/challenges/minimum-index-difference
import collections
n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
#list to dictionary
a = dict(enumerate(A))
b = dict(enumerate(B))
diff=100000
diff_key=0
#reverse key value of dictionary
a1 = {v: k for k, v in a.items()}
b1 = {v: k for k, v in b.items()}

for x in a1.keys():
    c=abs(a1[x]-b1[x])
    if c<diff:
        diff=c
        diff_key=x
    elif c==diff:
        if x<diff_key:
            diff=c
            diff_key=x
print(diff_key)


# print(a,b)
# print(a1,b1)
