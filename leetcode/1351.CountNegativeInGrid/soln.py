class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid)-1, len(grid[0])-1
        res, target = 0, -1
        for row in grid:
            # we will do binary search to find -1 in this row
            low, high = 0, n
            while low <= high:
                mid = (low + high)//2
                if target < row[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            gLow = low
            # if negative exist in the row, we add the number 
            # of negative elements to result.
            if gLow <= n:
                res += (n+1)-gLow
        return res
    
    # O(m+n) solution
    # def countNegatives(self, grid):
    #     i = len(grid)-1
    #     j = 0
    #     count = 0
    #     while i>=0 and j< len(grid[0]):
    #         print(i,j)
    #         if grid[i][j] < 0:
    #             count +=len(grid[0])-j
    #             i -= 1
    #         else:
    #             j +=1
    #     return(count)
