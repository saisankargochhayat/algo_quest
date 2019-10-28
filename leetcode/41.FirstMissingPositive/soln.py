class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:        
        # that array is adding zero. 
        nums.append(0)
        n = len(nums)
        # remove all the negatives and elements that are above the length of the array size.
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        # we are hashing the number of numbers enountered in the list. 
        for x in range(len(nums)):
            nums[nums[x]%n]+=n
        # print(nums)
        # we find the first encounter of zero and return.
        for i in range(1, len(nums)):
            if nums[i]//n == 0:
                return i
        return n
    
    # Hashing method
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         if not len(nums):
#             return 1
#         maxVal = max(nums)
#         dummyArray = {}
#         for i in nums:
#             if i >= 0:
#                 dummyArray[i] = True
#         for x in range(1, maxVal):
#             if x not in dummyArray:
#                 return x
#         else:
#             return maxVal + 1 if maxVal > 0 else 1
        
