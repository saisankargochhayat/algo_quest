class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set() # visited cells here
        res = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):  # val is basically grid[r, c]
                if val and (r,c) not in seen:  # if val is 1 and not visited already
                    # We do the iterative DFS here. 
                    stack = [(r,c)]
                    currArea = 0
                    while stack:
                        r0, c0 = stack.pop()
                        if (r0, c0) in seen:
                            continue
                        currArea += 1
                        for nr, nc in ((r0, c0-1), (r0-1, c0), (r0, c0+1), (r0+1, c0)):
                            if (0<=nr<len(grid) and 0<=nc<len(row)): # Check boundary conditions
                                if grid[nr][nc] and (nr, nc) not in seen: # check if val == 1 and not visited
                                    stack.append((nr, nc))
                        seen.add((r0, c0))
                    res = max(res, currArea)
        return res
                    
