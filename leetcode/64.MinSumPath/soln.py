class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0]*col for i in range(row)]
        minPath = 0
        return self.findPath(grid, row-1, col-1, dp)
        
        
    def findPath(self, grid, i, j, dp):
        #print(i,j, minPath)
        if dp[i][j]:
            return dp[i][j]
        if i == 0 and j == 0:
            dp[i][j] = grid[i][j]
            return grid[i][j]
        elif i == 0:
            dp[i][j] = grid[i][j] + self.findPath(grid, i,max(0,j-1), dp)
            return dp[i][j] #element to left
        elif j == 0:
            return self.findPath(grid, max(0,i-1),j, dp)+grid[i][j] #element on top
        else:
            a = self.findPath(grid, i,max(0,j-1), dp)+grid[i][j] #element to left
            b = self.findPath(grid, max(0,i-1),j, dp)+grid[i][j] #element on top
            dp[i][j] = min(a,b)
            return dp[i][j]
