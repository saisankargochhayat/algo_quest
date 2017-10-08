#input
n,m=map(int,input().split())
A = [[0 for x in range(m)] for y in range(n)]
# print(A)
mx=0;
c=0;
def maxcheck(c):
    global mx
    if c>=mx:
        mx=c
    else:
        c=0
#array input taken and stored
for i in range(n):
    A[i]=input().split()
for i in range(n):
    for j in range(m):
        #find all 2
        if A[i][j]=='2':
            x=i
            y=j
            #left direction
            while A[x][y]!='1' and y>0:
                while A[x][y-1]=='0':
                    y=y-1
                    c=c+1
            maxcheck(c)
            #right direction
            x=i
            y=j
            while A[x][y]!='1' and y<m:
                while A[x][y+1]=='0':
                    y=y+1
                    c=c+1
            maxcheck(c)
            #upwards
            x=i
            y=j
            while A[x][y]!='1' and x>0:
                while A[x-1][y]=='0':
                    x=x-1
                    c=c+1
            maxcheck(c)
            #downwards
            x=i
            y=j
            while A[x][y]!='1':
                while A[x+1][y]=='0' and x<n:
                    x=x+1
                    c=c+1
            maxcheck(c)
print(max)
