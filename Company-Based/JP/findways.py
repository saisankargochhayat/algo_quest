# Ways a string can be decoded "12" -> "ab", "l"

import sys
letterMap = {}
for i in range(0, 26):
    letterMap[i+1] = chr(i+97)

def findWays(s, res, currStr, i):
    # print(s)
    # print(currStr, i, res)
    if i >= len(s)-1:
        res.add(currStr)
        return
    if i == len(s)-1:  # We have reached end of string
        currStr += letterMap[int(s[i])]
        res.add(currStr)
        return
    # Check i, i+1 <= 26
    twoDigits = int(s[i]+s[i+1])
    if twoDigits <= 26:
        findWays(s, res, currStr+letterMap[int(twoDigits)], i+2)
    #Always check for i
    findWays(s, res, currStr+letterMap[int(s[i])], i+1)
    
    
lineS = ['123']

for line in lineS:
    # print(line, end="")
    res = set()
    findWays(str(line), res, '', 0)
    print(res)
    print(len(res))
    


