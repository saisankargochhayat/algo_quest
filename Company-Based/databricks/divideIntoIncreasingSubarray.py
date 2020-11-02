# Given an array arr[] consisting of non-negative integers, the task is to find the number of ways to 
# split the array into three non-empty contiguous subarrays such that their respective sum of elements are in increasing order.
def divideIncSubarray(arr):
    n = len(arr)
    # Find prefix sum
    calcPrefixSum = [arr[0]]
    for i in range(1,n):
        calcPrefixSum.append(calcPrefixSum[i-1]+arr[i])
    # Find suffix sum
    calcSuffixSum = [0 for i in range(n)]
    calcSuffixSum[n-1] = arr[n-1]
    for j in range(n-2, -1, -1):
        calcSuffixSum[j] = calcSuffixSum[j+1] + arr[j]
    
    pass



print(divideIncSubarray([2, 3, 1, 7]))