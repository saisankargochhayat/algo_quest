class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums[start:stop]
        # nums[-k:]  starts from kth last element in list
        k = k%len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        
        # nums[:] = [1,2,3] operating will edit the list as a references (they share same memory area)
        # nums = [1,2,3], you just give the reference of [1,2,3] to nums, after this nums doesn't reference the old list (a) any more
