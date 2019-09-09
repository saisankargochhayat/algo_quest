

# def calcRadiation(cArray):
#     radiationArray = [0 for i in range(len(cArray))]
#     for i in range(len(cArray)):
#         scope = cArray[i]
#         while scope > 0:
#             lowerBoundary = i - scope
#             higherBoundary = i + scope
#             if (0 <= lowerBoundary < len(radiationArray)):
#                 radiationArray[i-scope] += 1
#             if (0 <= higherBoundary < len(radiationArray)):
#                 radiationArray[i+scope] += 1
#             scope -= 1
#         radiationArray[i] += 1
#     return radiationArray
def calcRadiation(cArray):
    radiationArray = [0 for i in range(len(cArray))]
    index = 0
    lenOfCarray = len(radiationArray)
    value = lenOfCarray
    while index < lenOfCarray:
        radiationArray[index] = value
        index += 1
        if (index >= lenOfCarray):
            break
        else:
            radiationArray[index] = value
            index += 1
            value -= 1
    return radiationArray
    
    
noOfTestCases = int(input())
while noOfTestCases > 0:
    inputSize = int(input())
    cArray = list(map(int, input().strip().split()))
    zombieHealth = list(map(int, input().strip().split()))
    radiationArray = calcRadiation(cArray)
    sortedRadiation = sorted(radiationArray)
    sortedZombie = sorted(zombieHealth)
    if (sortedZombie == sortedRadiation):
        print("YES")
    else:
        print("NO")
    noOfTestCases -= 1

