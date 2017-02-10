






t=int(input())
for i in range(t):
    arr=list()
    N,X=map(int,input().split())
    for j in range(N):
        num=int(input())
        arr.append(num)
    subarray(arr,N,X)
