# So the problem is essentially 2 separate cases.

# But it's important to keep in mind that the L+M maximum could be reached before L & M separate from each other
# So you cannot divide each case into simply 2 steps:

# find the global maximum of the window on the left
# find the maximum of the second window in the region to the right of the first window
# case 1: L-window comes before M-windows
# Once L-window reaches it's global maximum, it will stop sliding but M window can keep going on

# case 2: M-window comes before L-windows
# Once M-window reaches it's global maximum, it will stop sliding but L window can keep going on


# We try leveraging knowledge form maximum subset sum for a window knowledge. 
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        pSum = [A[0]]  # Prefix sum
        for i in range(1, len(A)):
            pSum += [pSum[i-1] + A[i]]
        
        # Initialize [[_______L_____][__M__]____]  initial we assume l is first and then m
        res, lMax, mMax = pSum[L+M-1], pSum[L-1], pSum[M-1]  
        
        # window  | --- L --- | --- M --- |
        for i in range(L+M, len(A)):
            lMax = max(lMax, pSum[i-M] - pSum[i-L-M]) # This ensures lMax, new L compared. 
            # Now when lMax is reached, we want to maximize mMax
            res = max(res, lMax + pSum[i] - pSum[i-M])
        
        # window  | --- M --- | --- L --- |
        for j in range(L+M, len(A)):
            mMax = max(mMax, pSum[j-L] - pSum[j-L-M]) # We maximize mMax here
            res = max(res, mMax + pSum[j] - pSum[j-L])  # Now the maximized lMax
        
        return res
        