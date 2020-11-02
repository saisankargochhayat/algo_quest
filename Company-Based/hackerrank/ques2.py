# Box fitting
def findDolls(size):
    size.sort()
    largest = size[-1]
    largestSmallerBox = largest//2
    i = len(size)-1
    lowerIndex, higherIndex = 0, len(size)-1
    while(i > 0):
        if size[i] <= largestSmallerBox:
            lowerIndex = i
            break
        else:
            i -= 1
    # We found lower index and we have higherIndex(largest box)
    count = 0 # Number of boxes that can be fit
    while lowerIndex >= 0 and higherIndex > lowerIndex:
        if size[lowerIndex] <= (size[higherIndex]//2):
            count += 1
            lowerIndex -= 1
            higherIndex -= 1
        else:
            # cant fit so look for a smaller box
            lowerIndex -= 1
    return len(size)-count



print(findDolls([1, 2, 3, 5, 6, 6, 8, 9]))
print(findDolls([1,2,2,2,2,2,2,3]))