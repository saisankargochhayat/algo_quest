#Here are some naive O(n) and space O(1) Solutions

# Using sum idea.       
class Solution:
    def singleNumber(self, nums):
        return (3 * sum(set(nums)) - sum(nums)) // 2

        
# Naive hashmap solution. 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import defaultdict
        memory = defaultdict(int)
        for num in nums:
            memory[num] += 1
        for k,v in memory.items():
            if v == 1:
                return k

# 3 Duplicates and one unique value. 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t1, t2 = 0, 0
        for num in nums:
            t1 = (~t2) & (t1 ^ num)
            t2 = (~t1) & (t2 ^ num)
        return t1

# Generalizing for 5 duplicates and one unique value. 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t1, t2, t3, t4 = 0, 0, 0, 0
        for num in nums:
            t1 = (~t4 | ~t2 | ~t3) & (t1 & num)
            t2 = (~t1 | ~t4 | ~t3) & (t2 & num)
            t3 = (~t1 | ~t2 | ~t4) & (t3 & num)
            t4 = (~t1 | ~t2 | ~t3) & (t4 & num)
        return t1