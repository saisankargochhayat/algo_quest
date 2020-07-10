# # DP Solution 

# Approach 2: Dynamic Programming
# Intuition
# Preliminary computations in Approach 1 are quite heavy, and could be optimised with dynamic programming.
# Let's start from the array of ugly numbers which contains just one number - 1. 
# Let's use three pointers i2i_2i2​, i3i_3i3​ and i5i_5i5​, to mark the last ugly number which was multiplied by 2, 3 and 5, correspondingly.
# The algorithm is straightforward: choose the smallest ugly number among 2×nums[i2]2 \times \textrm{nums}[i_2]2×nums[i2​], 3×nums[i3]3 \times \textrm{nums}[i_3]3×nums[i3​], and 5×nums[i5]5 \times \textrm{nums}[i_5]5×nums[i5​] 
# and add it into the array. 
# Move the corresponding pointer by one step. Repeat till you'll have 1690 ugly numbers.
class Solution:
    def nthUglyNumber(self, n):
        res = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(1690):
            ugly = min(res[i2]*2, res[i3]*3, res[i5]*5)
            res.append(ugly)
            if ugly == res[i2] * 2:
                i2 += 1
            if ugly == res[i3] * 3:
                i3 += 1
            if ugly == res[i5] * 5:
                i5 += 1
        return res[n-1]

# Heap Solution
# from heapq import heappop, heappush
class Solution:
    def nthUglyNumber(self, n):
        seen = {1, }
        nums = nums = []
        heap = []
        heappush(heap, 1)

        for _ in range(n):
            curr_ugly = heappop(heap)
            nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)
            print(heap)
        return nums[n - 1]

# Slightly Better still times out
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         from collections import deque
#         # We will store ugly numbers here
#         res = [1]
#         resCopy = set([1])
#         twos, threes, fives = deque(), deque(), deque()
#         while len(res) < n:
#             lastNum = res[-1]
#             twos.append(lastNum * 2)
#             threes.append(lastNum * 3)
#             fives.append(lastNum * 5)
#             if twos[0] <= threes[0] and twos[0] <= fives[0]:
#                 if twos[0] not in resCopy:
#                     res.append(twos[0])
#                     resCopy.add(twos[0])
#                 twos.popleft()
#             elif threes[0] <= twos[0] and threes[0] <= fives[0]:
#                 if threes[0] not in resCopy:
#                     res.append(threes[0])
#                     resCopy.add(threes[0])
#                 threes.popleft()
#             else:
#                 if fives[0] not in resCopy:
#                     res.append(fives[0])
#                     resCopy.add(fives[0])
#                 fives.popleft()
#         print(res)
#         return res[-1]


# Brute Force
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         curr, num = 1, 1
#         while num <= n:
#             if self.isUgly(curr):
#                 num += 1
#             curr += 1
#         return curr-1
                
#     def isUgly(self, num: int) -> bool:
#         multiples = [30, 15, 6, 5, 3, 2]
#         for x in multiples:
#             while x <= num and num % x == 0:
#                 num /= x
#         return True if num == 1 else False

soln = Solution()
print(soln.nthUglyNumber(100))