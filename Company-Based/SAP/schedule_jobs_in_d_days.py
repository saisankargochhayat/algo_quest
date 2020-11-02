# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
# https://medium.com/@chuncaohenli/1335-minimum-difficulty-of-a-job-schedule-5ee30d10a88b
# didnt understand comeback to it
# The question wants you to divide array into d partitions such that max of each partioned summed up is minimized. 
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1  # We cant divide jobs into d partions
        dp = [[0] * n] + [[float('inf')] * n for _ in range(d - 1)]
        dp[0][0] = jobDifficulty[0] # 1 job in 1 day
        # For the first row, we calculate the the maxDifficulty to do jobDifficulty[:j+1] tasks in 1 day.
        for j in range(1, n):
            dp[0][j] = max(jobDifficulty[j], dp[0][j-1]) # max of current and last element. 
        
        for i in range(1, d): # for the rows of days
            for j in range(1, n): # for the columns of jobs
                max_r = jobDifficulty[j]
                print(i,j)
                for r in range(j, i-1, -1): # r goes back from j to i
                    max_r = max(max_r, jobDifficulty[r])
                    dp[i][j] = min(dp[i][j], max_r + dp[i - 1][r - 1])
                print(dp)
                
        # print(dp)
        return dp[-1][-1]

