#!/bin/python3

import sys
def check(s):
    toCheck = "hackerrank"
    j=0
    for i in range(len(s)):
        if s[i]==toCheck[j] and j<len(toCheck) :
            j+=1
        if j == len(toCheck):
            return('YES')
    return('NO')
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    print(check(s))