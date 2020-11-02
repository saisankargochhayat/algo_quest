# Get prefix sum array, find n-k window for which n-k is minimum.           
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        pSum = [0] * n
        pSum[0] = cardPoints[0]
        for i in range(1, n):
            pSum[i] = cardPoints[i] + pSum[i-1]
        wSize = n-k # window size to minimize
        minNK = pSum[wSize-1]
        # We minimize n-k 
        for i in range(wSize, n):
            minNK = min(minNK, pSum[i]-pSum[i-wSize])
        return pSum[n-1] - minNK
            
 

# Times out, but works. 
from functools import lru_cache
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        # Helps find the maximum score. 
        @lru_cache(maxsize=None)
        def helper(l, r, k, score):
            # print(cardPoints[l:r+1], k, score)
            # Base condition 
            if k == 0:
                return score
            pickingLeft = helper(l+1, r, k-1, score+cardPoints[l])
            pickingRight = helper(l, r-1, k-1, score+cardPoints[r])
            return max(pickingLeft, pickingRight)
        
        return helper(0, len(cardPoints)-1, k, 0)
            

