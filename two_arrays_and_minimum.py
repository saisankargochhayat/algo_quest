#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/two-arrays-and-minimum/
import sys
def main():
    abc=list(map(int,input().split()))
    a=abc[0]
    b=abc[1]
    c=abc[2]
    n=int(input())
    A=list()
    B=list()
    #generating both arrays
    A.append(a*c)
    B.append(b*c)
    for i in range(1,n):
        temp=A[i-1]*a*b*c + A[i-1]*a*b + A[i-1]*a*c
        A.append(int(temp))
        A[i] = A[i]%1000000007
        B.append(int(B[i-1]*b*c*a + B[i-1]*b*a + B[i-1]*b*c))
        B[i] = B[i]%1000000007
    # print(A)
    # print(B)
    small1=sys.maxsize
    small3=sys.maxsize
    small2=sys.maxsize
    small4=sys.maxsize
    for i in range(len(A)):
        if A[i]<small1:
            small2=small1
            small1=A[i]
            index1=i
        elif (A[i]<small2 and A[i]!=small1):
            small2=A[i]

    for j in range(len(B)):
        if B[j]<small3:
            small4=small3
            small3=B[j]
            index2=j
        elif (B[j]<small4 and A[i]!=small3):
            small4=B[j]
    #print(small1,small2,small3,small4)
    if index1!=index2:
        print(small1+small3)
    else :
        if (small1+small4)>(small3+small2):
            print(small3+small2)
        else :
            print(small1+small4)



main()
