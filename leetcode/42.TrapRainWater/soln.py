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
