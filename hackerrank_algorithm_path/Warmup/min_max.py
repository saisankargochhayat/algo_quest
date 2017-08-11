#https://www.hackerrank.com/challenges/mini-max-sum
#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
arr.sort()
sum = sum(arr)
print(sum-arr[4],sum-arr[0])
