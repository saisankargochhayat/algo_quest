class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if sortedHeights[i] != heights[i]:
                       ans += 1
        return ans
