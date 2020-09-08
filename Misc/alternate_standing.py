#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/i-demand-trial-by-combat-13/
t=(int(input()))
a=1
b=0
prev=list()
prev1=list()
for i in range(t):
    n=list(map(int,input().split()))
    #6,2
    o=list()
    m=list(map(int,input().split()))
    for k in range(n[1]):
        m.insert(0,a)
        m[len(m):] = [a]
        for j in range(1,n[0]+1):
            if m[j-1]==1 and m[j+1]==1:
                o.append(a)
            else :
                o.append(b)
        prev1=prev
        prev=m[1:n[0]+1]
        #print(prev)
        #compares array
        if prev==o:
            m=prev
            break
        if prev1==o:
            if (n[1]-k)%2==0:
                m=prev
            else:
            	m=o
            break
        del m[:]
        m=list(o)
        del o[:]
        #prints elements of a list

    print(*m, sep=' ')
