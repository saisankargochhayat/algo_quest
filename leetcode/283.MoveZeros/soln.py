class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        So the idea is, we are keeping a partition, and all non zero elements are pushed just behind the partition. 
        """
        partition = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[partition] = nums[partition], nums[i]
                # Push partition further.
                partition += 1
        
    
