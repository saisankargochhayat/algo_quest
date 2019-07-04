class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min1 = float('inf')
        min2 = float('inf')
        
        if (len(nums) < 3):
            return False
        
        for num in nums:
            if num < min1:
                min1 = num
            
            if num > min1:
                min2 = min(min2, num)
            
            if num > min2:
                return True