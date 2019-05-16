n = int(input())
countmap = dict()
for i in range(n):
    countmap[i]=0
arr = list(map(int,input().strip().split()))
for i in arr:
    countmap[i]+=1
ans = ""
for i in range(100) :
    ans = ans+str(countmap[i])+" "
print(ans.strip())