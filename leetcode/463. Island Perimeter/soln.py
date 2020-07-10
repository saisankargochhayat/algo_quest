class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Dimensions of the grid
        r, c = len(grid), len(grid[0])
        perimeter = 0
        # Lets find the perimeter now   
        for m in range(r):
            for n in range(c):
                if grid[m][n] == 1:
                    adj = []
                    adj.append([m, max(0, n-1)])  # left
                    adj.append([m, min(n+1, c-1)]) # right
                    adj.append([min(m+1, r-1), n])  # bottom
                    adj.append([max(m-1, 0), n])  # above
                    for i, j in adj:
                        if grid[i][j] == 0 or (i==m and j==n):
                            perimeter = perimeter + 1
        return perimeter

# Better solution, only check left and upper. 
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    
                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2
                        
                    if c > 0 and grid[r][c-1] == 1:
                        result -= 2
        
        return result
