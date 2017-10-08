# a=[1,2,3,4,5,6,7,8,8,9]
# b=[1,2,3,4,5,6,7,8,8,9]
# if a==b:
#     print("hello")
# else:
#     print("not equal")

# n=int(input())
# for i in range(n):
#     x=int(input())
#     if x==1:
#         print("Yes")
#     elif x%2==0:
#         print("Yes")
#     else:
#         print("No")

def pattern(inputv):
    if not inputv:
        return inputv

    nxt = [0]*len(inputv)
    for i in range(1, len(nxt)):
        k = nxt[i - 1]
        while True:
            if inputv[i] == inputv[k]:
                nxt[i] = k + 1
                break
            elif k == 0:
                nxt[i] = 0
                break
            else:
                k = nxt[k - 1]

    smallPieceLen = len(inputv) - nxt[-1]
    if len(inputv) % smallPieceLen != 0:
        return inputv

    return inputv[0:smallPieceLen]
print(pattern("bcbdbcbcbdbc"))
