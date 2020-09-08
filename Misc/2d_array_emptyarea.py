import math
n=int(input())
ans=0
#initializing array with zeros
A = [[0 for x in range(n)] for y in range(n)]
emp=list()
for i in range(n):
    A[i]=input()

for i in range(n):
    for j in range(n):
        if A[i][j]=='.':
            emp.append((i,j))
    # print("\n")
def center(x,y,A,r):
    for i in range(x-r,x+r+1):
        for j in range(y-r,y+r+1):
            if not isAvailable(i,j,x,y,A,r):
                return False

    return True



def distan(i,j,x,y):
    return math.sqrt((y-j)**2 + (x-i)**2)
def isAvailable(i,j,x,y,A,r):
    if i<0 or i >=n or j<0 or j>=n:
        return False
    dist=distan(i,j,x,y)
    if dist>r:
        return True
    if A[i][j]==".":
        return True
    return False
for i in range(len(emp)):
    x=emp[i][0]
    y=emp[i][1]
    radius=1
    while center(x,y,A,radius):
        if (radius>ans):
            ans=radius
        radius+=1

print(ans)
