class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum, currSum = sum(nums), 0
        for i, num in enumerate(nums):
            if totalSum - num == 2*currSum:
                return i
            currSum += num
        return -1
            
            
    # def pivotIndex(self, nums: List[int]) -> int:
    #     if nums:
    #         fCounter = 0
    #         bCounter = 0
    #         l = len(nums)
    #         fNums = []
    #         bNums = []
    #         for i in range(l):
    #             fCounter += nums[i]
    #             fNums.append(fCounter)
    #             bCounter += nums[l-i-1]
    #             bNums.append(bCounter)
    #         bNums = bNums[::-1]
    #         if l >= 2:
    #                 if bNums[1] == 0:
    #                     return 0                
    #         for i in range(1,l-1):
    #             if fNums[i-1] == bNums[i+1]:
    #                 return i
    #         if l >= 2:
    #             if fNums[l-2] == 0:
    #                 return l-1  
    #     return -1
