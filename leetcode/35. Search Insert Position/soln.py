class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binHelper(low, high, x):
            mid = low + (high - low)//2
            if low > high:
                return low
            if nums[mid] == x:
                return mid
            elif nums[mid] > x:
                return binHelper(low, mid-1, x)
            elif nums[mid] < x:
                return binHelper(mid+1, high, x)          
        low, high = 0, len(nums)-1
        return binHelper(low, high, target)
       
