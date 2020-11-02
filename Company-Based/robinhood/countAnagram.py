# Given an array s[] of N strings. The task is to find the number of pairs of indices (i, j) such that s[i] is an anagram of s[j].

# Examples:

# Input: s[] = {“aaab”, “aaba”, “cde”, “dec”}
# Output: 2
# (“aaab”, “aaba”) and (“cde”, “dec”) are the only valid pairs.

# Input: s[] = {“ab”, “bc”, “cd”}
# Output: 0

import math

def countAnagram(arr):
    from collections import defaultdict
    mem = defaultdict(int)
    for word in arr:
        temp = ''.join(sorted(word))
        mem[temp] += 1
    res = 0
    for k in list(mem.values()):
        res += k*(k-1)//2
        # Less optimal
        #res += int(math.factorial(k)/(2*math.factorial(k-2)))
    return res




print(countAnagram(['aaab', 'aaba', 'cde', 'dec']))