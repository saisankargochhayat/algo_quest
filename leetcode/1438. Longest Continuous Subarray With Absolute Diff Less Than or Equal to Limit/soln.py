# Two Pointer
# The trick is to maintain min and max for a window. 
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        res = 0
        l, r = 0, 0
        minDQ, maxDQ = deque(), deque()
        while r < len(nums):
            while minDQ and nums[r] <= nums[minDQ[-1]]:
                minDQ.pop()  # Ensures monotonically increasing queue if anything lesser than min pop
            while maxDQ and nums[r] >= nums[maxDQ[-1]]:
                maxDQ.pop() # Ensures monotonically decreasing queue if anything greater than right then pop
            maxDQ.append(r)
            minDQ.append(r)
        
            # Move left
            
            while (nums[maxDQ[0]] - nums[minDQ[0]]) > limit:
                l += 1
                if l > minDQ[0]:
                    minDQ.popleft()  # Remove elements from index less than l
                if l > maxDQ[0]:
                    maxDQ.popleft()
            print(minDQ, maxDQ)
            res = max(res, r-l+1)
            r += 1

        return res


# More Slow Soutions
# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         from collections import deque
#         res = 0
#         l, r = 0, 0
#         minDQ, maxDQ = deque(), deque()
#         while r < len(nums)+1:
#             subList = nums[l:r]
#             if subList:
#                 currMax = max(subList)
#                 currMin = min(subList)

#                 while (currMax - currMin) > limit:
#                     l += 1
#                     subList = nums[l:r]
#                     currMax = max(subList)
#                     currMin = min(subList)

#             res = max(res, r-l)
#             r += 1

#         return res

            

            

            
# Slow solution
# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         allSublists = [[]]
#         res = 0
#         # Generate all sublists
#         for i in range(len(nums)+1):
#             for j in range(len(nums), i, -1):
#                 subList = nums[i:j]
#                 # allSublists.append(sublist)
#                 currMin = min(subList)
#                 currMax = max(subList)
#                 if (currMax - currMin) <= limit:
#                     res = max(res, len(subList))
#                     break # from this loop because other sublists will be smaller anyway
#         return res
