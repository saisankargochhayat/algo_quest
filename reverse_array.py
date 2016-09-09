import numpy as np

n=(int(input()))
arr = [int(input()) for _ in range(n)]
#arr = list(map(int, input().split()))
# print(arr)
for a in reversed(arr):
    print(a)
