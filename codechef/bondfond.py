#https://www.codechef.com/LOCMAY17/problems/BONDFOND
n=int(input())
for t in range(n):
    m=int(input())
    i=0
    while(True):
        if m < 2**i:
            i=i-1
            break
        else:
            i+=1
    c=abs(2**i - m)
    d=abs(2**(i+1) - m)
    print(min(c,d))
