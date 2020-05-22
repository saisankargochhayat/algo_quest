from typing import List
# Using backtracking
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # curr = current elements in the iteration.
        # elements = remaining elements to be considered. 
        # added = list of indicaters whether element added to curr or not. 
        def permute_helper(curr, added):
            # base condition
            if len(curr) == l:
                res.append(curr[:])
            for i in range(l):
                if not added[i]:
                    # We add the element to curr
                    curr.append(nums[i])
                    added[i] = True
                    permute_helper(curr, added)
                    # Now we backtrack to remove that element to add another element like [1,2] to [1] and then move to [1,3]
                    curr.pop()
                    added[i] = False

        res = []
        l = len(nums)
        added = [False]*len(nums)
        permute_helper([], added)
        return res

    # Without using backtracking
    # import itertools
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     res = list(itertools.permutations(nums))
    #     return res


soln = Solution()
print(soln.permute([1,2,3]))