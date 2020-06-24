class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right, maxCount = 0, 0, 0
        while right < len(A):
            if A[right] == 0:
                K -= 1
            # Only after its below zero we shrink, to utilize max num of zeros. 
            while K < 0:
                # We start shrinking here
                if A[left] == 0:
                    K += 1
                left += 1
            maxCount = max(right-left+1, maxCount)
            # We expand here. 
            right += 1
        return maxCount
