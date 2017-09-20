#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if (v1-v2) is not 0:
        re = (x2-x1)/(v1-v2)
    else:
        return('NO')
    if re>0 and (re==int(re)):
        return('YES')
    else:
        return('NO')

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
