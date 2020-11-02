def maxBalancedTeams(developers, maxNewHires):
    maxCount = 0
    developers.sort() # We sort developers to figure out where to add. 
    for i in range(len(developers)-1, -1, -1):
        newCopy = maxNewHires
        curr = 0
        pointer, pVal = i, developers[i]
        while (pVal - developers[pointer]) <= newCopy and pointer >= 0:
            curr += 1
            newCopy -= (pVal - developers[pointer])
            pointer -= 1
        if curr == len(developers):
            return curr
        maxCount = max(maxCount, curr)
    return maxCount

print(maxBalancedTeams([3, 0, 2, 2, 1], 3)) # 4
print(maxBalancedTeams([1, 1, 1], 7))  # 3
print(maxBalancedTeams([5, 4, 1, 3, 4], 2))  # 3
print(maxBalancedTeams([1, 2, 2, 2, 2, 3], 4))  # 5