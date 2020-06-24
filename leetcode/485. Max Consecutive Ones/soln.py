class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes, c = 0, 0 
        for num in nums:
            if num == 1:
                c += 1
                maxOnes = max(maxOnes, c)
            else:
                c = 0
        return maxOnes
