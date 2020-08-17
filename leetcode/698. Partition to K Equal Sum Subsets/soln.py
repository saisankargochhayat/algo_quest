# Backtracking Approach
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        target = s//k
        seen = [False] * len(nums)
        # k in the num of buckets remaining to fill. 
        return self.canPartition(nums, k, seen, target, 0, 0)
            
            
    def canPartition(self, nums, k, seen, targetSubsetSum, currSubsetSum, nextIndex) -> bool:
        # Base conditions, if all buckets are filled. We can a;so stop at k == 1
        # if k-1 buckets are filled, the last one can be filled with rest of the elements
        if k == 0:
            return True
        if currSubsetSum == targetSubsetSum:
            # One less bucket to fill, currSubsetSum reset to 0, nextIndex reset to 0
            return self.canPartition(nums, k-1, seen, targetSubsetSum, 0, 0)
        for i in range(nextIndex, len(nums)):
            if not seen[i] and currSubsetSum + nums[i] <= targetSubsetSum:
                seen[i] = True
                # Propagate True back. 
                if self.canPartition(nums, k, seen, targetSubsetSum, currSubsetSum + nums[i], i+1):
                    return True
                # Else we backtrack here 
                seen[i] = False
        
        # No combination of subsets can achieve equal sums
        return False
        
    
