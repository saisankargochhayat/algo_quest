def is_perfect( value, exponent ):
    root = value ** ( 1.0 / exponent )
    root = long( round( root ) )
    if root ** exponent  == value:
        return root
    else:
        return -1

p=int(raw_input())
while p:
    m,n=map(int, raw_input().split())
    p=p-1
    r=is_perfect(n,m)
    print r
    # if :
    #     print int(r)
    # else:
    #     print -1
