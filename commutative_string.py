#https://www.hackerrank.com/contests/w23/challenges/commuting-strings
#function to find smallest repeating pattern in string
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
count=0
word=input()
m=int(input())
new=pattern(word)
count=m/len(new)
print(int(count))
