#https://www.codechef.com/SNCKQL17/problems/TEMPLELA
def checkeven(m):
    if m%2==0:
        return 1
    else:
        return 0
def cmp(a, b):
    return (a > b) - (a < b) 
def main():
    n=int(input())
    for i in range(n):
        m=int(input())
        j=list(map(int, input().split()))
        if checkeven(m):
            print("no")
        else:
            #new list to compare with input
            l=[]
            for k in range(1,m+1):
                if k <= (m+1)/2:
                    l.append(k)
                elif k>(m+1)/2:
                    l.append((m+1)-k)
            if cmp(j,l)==0:
                print("yes")
            else:
                print("no")
            del l[:]
main()


