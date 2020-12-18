# A smart string is one with characters in strictly increasing or decreasing order. 
# Given a string M, we need to determine the minimum number of contiguous substrings in which M can be broken so that each substring is smart.

# Examples: Input: abcdcba
# Output: 2

# partitioned into abc and dcba

# Input: ffdhbbbdeeggbb
# Output:4

# 1 is uphill 0 is downhill -1 ambigious

def smartStrings(s: str):
    res, grad = 1, 0
    for i in range(1, len(s)):    
        if s[i] > s[i-1]:   # Increasing slope starts/continues
            if grad == 0:
                grad = 1  # ambigous to positive slope
            elif grad == -1:
                grad = 0
                res += 1
        elif s[i] < s[i-1]:  # Decreasing slope starts/continues
            if grad == 0:
                grad = -1
            elif grad == 1:
                grad = 0
                res += 1
        # print(s[i], res)
    return res
            




print(smartStrings("abcdcba"))
print(smartStrings("ffdhbbbdeeggbb"))
print(smartStrings("abcdabcdcbaaaa"))
print(smartStrings("dcbaaaabcdddddddccccbbbaaaa"))