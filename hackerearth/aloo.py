t = int(input())
for i in range(t):
    a,b = input().split(' ')
    a = int(a)
    b = int(b)
    x = b**(1/a)
    if x.is_integer():
        print(int(x))
    else:
        print(-1)
