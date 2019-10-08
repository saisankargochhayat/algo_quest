class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, currMin = 0, float('inf')
        for i in range(len(prices)):
            res = max(res, prices[i]-currMin)
            currMin = min(currMin, prices[i])
        return 0 if res<0 else res
