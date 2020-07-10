# N(logN) 
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedArr = sorted(nums)
        left = len(nums)
        right = 0
        for i in range(0, len(nums)):
            if nums[i] != sortedArr[i]:
                left = min(left, i)
                right = max(right, i)
        return right - left + 1 if right - left > 0 else 0

# N(logN) 
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedArr = sorted(nums)
        left = right = 0
        for i in range(0, len(nums)):
            if nums[i] != sortedArr[i]:
                left = i
                break
        for j in range(len(nums)-1, 0, -1):
            if nums[j] != sortedArr[j]:
                right = j
                break
        return right - left + 1 if right != left else 0

# Run - O(N) Space - O(N)
# Stack approach here we think of increasing slope and use a stack to go back. 
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        from collections import deque
        l, r = len(nums), 0
        stack = deque()
        for i in range(0, len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        stack.clear()
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] < nums[j]:
                r = max(r, stack.pop())
            stack.append(j)
        return r - l + 1 if r > l else 0


# Run - O(N) Space - O(1)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minVal = float(inf)
        maxVal = -float(inf)
        # Find min value in downward slope
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                minVal = min(minVal, nums[i])
        # Find max value in downward slope from other side. 
        for j in range(len(nums)-2, -1, -1):
            if nums[j] > nums[j+1]:
                maxVal = max(maxVal, nums[j])
        l, r = 0, 0
        # Now find left pos of minVal
        for i in range(0, len(nums)):
            if nums[i] > minVal:
                l = i
                break
         # Now find right pos of minVal
        for j in range(len(nums)-1, -1, -1):
            if nums[j] < maxVal:
                r = j
                break
        return r - l + 1 if r > l else 0