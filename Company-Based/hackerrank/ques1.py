def generateCombination(s: str):
    res = 0
    # Check first and last char are same
    res = res + 1 if s[0] == s[len(s)-1] else res
    fPointer, sPointer = 0, 1
    while sPointer < len(s):
        if s[fPointer] == s[sPointer]:
            res += 1
        fPointer += 1
        sPointer += 1
    return res


print(generateCombination("aaabbba"))
print(generateCombination("accbb"))
