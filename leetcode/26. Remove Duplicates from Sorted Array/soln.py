class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        i, j = 0, 1
        while j < l:
            if nums[j] != nums[i]:  # Update tail when encountered new element. 
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1
                
                
