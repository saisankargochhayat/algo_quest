## Idea is we move inner if height tends to increase for the min bar. 
# Start from both end, close in from the smaller side, if both are equal any side works. 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        start, end = 0, len(height)-1
        while start < end:
            res = max(res, ((end-start)*min(height[end], height[start])))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1         
        return res
            
        
