n = int(input())
countmap = dict()
for i in range(n):
    countmap[i]=0
arr = list(map(int,input().strip().split()))
m = len(arr)
for i in arr:
    countmap[i]+=1
prev = 0
for i in range(100):
    countmap[i]+=prev
    prev = countmap[i]
# print(countmap)
sorted_arr = [0]*n
for i in arr:
    sorted_arr[countmap[i]-1] = i
    countmap[i]-=1
# print(sorted_arr)

ans = ""
for i in range(n) :
    ans = ans+str(sorted_arr[i])+" "
print(ans.strip())