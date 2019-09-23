class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        local_min = nums[0]
        local_max = nums[0]
        global_max = nums[0]
        
        # Maintain local max, local min and global max!
        for i in range(1,len(nums)):
            # Once we have encountered a negative element we consider it by multiplying it. 
            # print(local_min, local_max, global_max)
            if nums[i] < 0:
                local_max, local_min = local_min, local_max
            
            local_min = min(nums[i], nums[i]*local_min)
            local_max = max(nums[i], nums[i]*local_max)
            
            global_max = max(global_max, local_max)
        return global_max
            
                
