#https://www.hackerrank.com/challenges/a-very-big-sum
#!/bin/python3
import sys

def aVeryBigSum(n, ar):
    # Complete this function
    c = 0
    for i in ar:
        c = c+i
    return c

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
