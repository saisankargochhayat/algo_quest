def subarray(arr,N,X):
    curr_sum=arr[0]
    # if curr_sum==X:
    #     print("YES")
    #     return 0
    start=0
    for i in range(1,N+1):
        while curr_sum>X and start<i-1:
            curr_sum=curr_sum-arr[start]
            start+=1
        if curr_sum==X:
            print("YES")
            return 0
        if i<N:
            curr_sum=curr_sum+arr[i]
    print("NO")
    return 0

t=int(input())
for i in range(t):
    arr=list()
    N,X=map(int,input().split())
    for j in range(N):
        num=int(input())
        arr.append(num)
    subarray(arr,N,X)
