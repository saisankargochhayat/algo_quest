t=(int(input()))
for i in range(t):
    s=input().split()
    N,M=int(s[0]),(s[1])
    m=M
    p=input()
    #prints list with space
    p =" ".join(p.split())
    p1, p2, p3 = 0, 0, 0
    for j in range(M):
        m -= 1
		x = len(p)
		x1, x2 = p[1], p[x - 2]
        print(x,x1,x2)
