#!/bin/python3

import sys
def odd(a):
    if a%2!=0:
        return True
    
def pythagoreanTriple(a):
    # Complete this function
    if odd(a):
        k=((a*a)-1)/2
        return a,int(k),int(k+1)
    else:
        k=((a/2)**2 -1)
        return a,int(k),int(k+2)
a = int(input().strip())
triple = pythagoreanTriple(a)
print (" ".join(map(str, triple)))

