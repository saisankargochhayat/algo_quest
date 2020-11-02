# So we create a DP and start from the last low and start building up the the upper rows in the dp 2d array
# dp[i][j] represents the minimum path to reach that element with the given constraints. 
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        dp = [[0 for j in range(len(A[0]))] for i in range(len(A))]
        # we fill the last row with original values as the min path from last row to last row is its own value
        for i in range(len(A)-1, -1, -1):
            for j in range(len(A[0])-1, -1, -1):
                # Fill last row
                if i == len(A)-1:
                    dp[i][j] = A[i][j]
                # left corner
                elif j == 0:
                    dp[i][j] = A[i][j] + min(dp[i+1][j], dp[i+1][j+1])
                elif j == len(A[0])-1:
                    dp[i][j] = A[i][j] + min(dp[i+1][j-1], dp[i+1][j])
                else:
                    dp[i][j] = A[i][j] + min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
        return min(dp[0])
