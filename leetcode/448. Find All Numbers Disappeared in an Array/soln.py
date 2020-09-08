class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            temp = abs(num) - 1 
            # if it has not been converted negative
            if nums[temp] > 0:
                nums[temp] *= -1
        # if we notice positive int, 
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res



# Using O(n) space
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        countDic = Counter(nums)
        res = [k if k not in countDic else None for k in range(1, len(nums)+1)]
        ans = list(filter(lambda x: x != None, res))
        return ans
            
