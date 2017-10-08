#!/bin/python3

import sys

def twinArrays(ar1, ar2):
    # Complete this function
    ar3=[[0 for i in range(2)] for j in range(len(ar1))]
    ar4=[[0 for i in range(2)] for j in range(len(ar2))]
    ar5=ar1.sort()[:]
    ar6=ar2.sort()[:]
    for i in len(ar5):
        ar3[i][0].append(ar5[i])
        ar3[i][0].append(ar1.index(ar5[i]))
    for i in len(ar6):
        ar4[i][0].append(ar6[i])
        ar4[i][0].append(ar2.index(ar6[i]))
    print(ar3)
    print(ar4)            

            
        
n = int(input().strip())
ar1 = list(map(int, input().strip().split(' ')))
ar2 = list(map(int, input().strip().split(' ')))
result = twinArrays(ar1, ar2)
print(result)
