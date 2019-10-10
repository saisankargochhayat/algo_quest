# Start with picking the first 1 you can find. 
# Pick that point and start dfs to all all the edges for that island. 
# Now start bfs on the elements and exit when we find the second island, and quit when next 1 is found.
class Solution:
    rows = 0
    col = 0
    A = 0
    def shortestBridge(self, A: List[List[int]]) -> int:
        self.col = len(A[0])
        self.rows = len(A)
        self.A = A
        bfs = [] 
        self.dfs(bfs, *self.first(self.rows, self.col))
        
        # Final bfs logic to start expanding from each of the nodes of the first island.
        count = 0
        while bfs:
            newBfsStack = []
            for i,j in bfs:
                for x,y in ((i-1, j),(i+1, j),(i, j-1),(i, j+1)):
                    if 0<=x<self.rows and 0<=y<self.col and self.A[x][y] == 1:
                        return count
                    elif 0<=x<self.rows and 0<=y<self.col and self.A[x][y] == 0:
                        self.A[x][y] = -1                     
                        newBfsStack.append((x,y))
            count += 1
            bfs = newBfsStack
        return count
         
                    
    # Returns the first 1 encoutnered in the matrix.
    def first(self, rows, col):
        for i in range(rows):
            for j in range(col):
                if self.A[i][j]:
                    return i,j
                
    # Adds all the 1 nodes in from the first coordinate to the bfs list. 
    def dfs(self, bfs, i, j):
        bfs.append((i,j))
        if self.A[i][j] == 1:
            self.A[i][j] = -1
            for i,j in ((i-1, j),(i+1, j),(i, j-1),(i, j+1)):
                if 0<=i<self.rows and 0<=j<self.col and self.A[i][j] == 1:
                    self.dfs(bfs,i,j)
        
                
    
        
        
        
        

    

