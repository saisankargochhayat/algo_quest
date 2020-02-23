# Backtracking - 
# 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            if len(curr) == k:
                # This is a shallow copy of the list.
                result.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()
        result = []
        n = len(nums)
        for k in range(n+1):
            backtrack()
        return result



# # Iterative solution
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = [[]]
#         nums_len = len(nums)
        
#         # The idea is to append every element to every other element in the 
#         # result list. This works because the list is distinct.
#         for i in range(nums_len):
#             result += [subset+[nums[i]] for subset in result]
        
#         return result
