class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        front, localSum = 0, 0 
        globalFront, globalBack = float('inf'), 0
        for back in range(len(nums)):
            while front < len(nums) and localSum < s:
                localSum += nums[front]
                front += 1
            if localSum >= s:
                if front-back < (globalFront-globalBack):
                    globalFront, globalBack = front, back
            localSum -= nums[back]
        if globalFront == float('inf'):
            return 0        
        return globalFront-globalBack
                    
