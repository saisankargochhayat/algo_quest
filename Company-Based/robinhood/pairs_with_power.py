# Given an array arr[] of positive integers, the task is to count the maximum possible number of pairs (arr[i], arr[j]) such that arr[i] + arr[j] is a power of 2.
# Note: One element can be used at most once to form a pair.

# Examples:

# Input: arr[] = {3, 11, 14, 5, 13}
# Output: 2
# All valid pairs are (13, 3) and (11, 5) both sum up to 16 which is a power of 2.
# We could have used (3, 5) but by doing so maximum of 1 pair could only be formed.
# Therefore, (3, 5) is not optimal.

# Input: arr[] = {1, 2, 3}
# Output: 1
# 1 and 3 can be paired to form 4, which is a power of 2.

import math
# Function to check 
# Log base 2 
def Log2(x): 
    return (math.log10(x) / math.log10(2))

def isPowerOfTwo(n):
    return math.ceil(Log2(n)) == math.floor(Log2(n))

def generateTwos(minRange, maxRange):
    twos = set()
    for i in range(minRange, maxRange+1):
        if isPowerOfTwo(i):
            twos.add(i)
    return twos

def count_max_pairs(nums):
    minRange = min(nums)*2
    maxRange = max(nums)*2
    powerOfTwos = generateTwos(minRange, maxRange)
    # Do two sum  here to find the numbers that add up to powerOfTwos
    
    print(powerOfTwos)

print(count_max_pairs([3, 11, 14, 5, 13]))