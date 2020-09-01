class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mem = [0]*101
        for num in nums:
            mem[num] += 1
        for i in range(1,101):
            mem[i] += mem[i-1]
        res = [0 if num==0 else mem[num-1] for num in nums]
        return res
        
            
            
        
