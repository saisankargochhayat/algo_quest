# import copy
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        # copyGrid = copy.deepcopy(grid)
        copyGrid = grid
        m = len(grid)
        n = len(grid[0])
        res = 0 
        for i in range(m):
            for j in range(n):
                if copyGrid[i][j] == "1":
                    res += 1
                    self.checkIsland(copyGrid, i, j, m-1, n-1)
        return res
    
    def checkIsland(self, copyGrid, i, j, m, n):
        if copyGrid[i][j] == "0":
            return
        else:
            copyGrid[i][j] = "0"
            # check top
            self.checkIsland(copyGrid, max(0, i-1), j, m, n)
            #check bottom
            self.checkIsland(copyGrid, min(m, i+1), j, m, n)
            #check left
            self.checkIsland(copyGrid, i, max(0, j-1), m, n)
            #check right
            self.checkIsland(copyGrid, i ,min(n, j+1), m , n)
        return
