class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        # base sorted case and single input cases [0]
        if nums[high] >= nums[0]:
            return nums[0]
        while low <= high:
            mid = (low + high)//2
            # print(low, mid, high)
            # Find if curr mid element if min element. 
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid-1] > nums[mid+1]:
                return nums[mid]
            # Modify high and low. 
            if nums[mid] < nums[low]:
                # Search left and point could only be left to this. 
                high = mid - 1
            elif nums[mid] > nums[high]:
                # Search right, as the min lies between the bigger element on mid
                # and middle element on high. 
                low = mid + 1