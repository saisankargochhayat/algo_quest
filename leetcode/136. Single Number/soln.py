# Using XOR Bitwise operator. 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr = nums[0]
        for i in range(1, len(nums)):
            curr = curr ^ nums[i]
        return curr
