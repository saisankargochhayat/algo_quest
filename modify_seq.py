#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/modify-sequence/
import math
def main():
    a=int(input())
    A=list()
    B=list()
    for k in range(a):
        b=int(input())
        count=0
        for i in range(1,b+1):
            A.append(i)
            B.append(i)
        # print(A)
        # print(B)
        for i in range(b):
            for j in range(b):
                # print("gcd of ",i+1,"and",j+1,"is=",gcd(A[i],B[j]))
                # print("kgcd of ",i+1,"and",j+1,"is=",kgcd(A[i],B[j]))
                if gcd(A[i],B[j])!=kgcd(A[i],B[j]):
                    count+=1
        print(int((b*b)-count))
        del A[:]
        del B[:]
        # print("gcd is=",gcd(a,b))
        # print("kgcd is=",kgcd(a,b))
def kgcd(x,y):
    while x>0 and y>0:
        x-=y
        x,y=y,x
    return x+y
def gcd(c,d):
    while c!=d:
        if c>d:
            c -= d;
        else:
            d -= c;
    return c
main()
