#https://www.hackerrank.com/contests/w23/challenges/treasure-hunting
x,y=map(float,input().split())
a,b=map(float,input().split())
a1=-b
b1=a
# print(a,b,a1,a2)
deter=(a*b1)-(b*a1)
dx=(x*b1)-(y*a1)
dy=(a*y)-(b*x)
m=dx/deter
n=dy/deter
print("%.12f" %m)
print("%.12f" %n)
