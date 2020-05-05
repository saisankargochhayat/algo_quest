from collections import deque
class Solution:
    # Two pointer approach
    def trap(self, height: List[int]) -> int:
        left, leftMax, right, rightMax = 0, 0, len(height)-1, 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    res += leftMax - height[left]
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    res += rightMax - height[right]
                right -= 1
        return res
    
    # Stack approach
    def trap(self, height: List[int]) -> int:
        mapStack = deque()
        res = 0
        for i,curr in enumerate(height):
            while mapStack and curr > mapStack[-1][1]:
                _, popped = mapStack.pop()
                if not mapStack:
                    break
                j, leftBorder = mapStack[-1]
                distance = i-j-1
                bounded_height = min(leftBorder-popped, curr-popped)
                res += bounded_height * distance
            # Append new element.
            mapStack.append((i,curr))
        return res
    
        
