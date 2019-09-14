class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Handling empty board.
        if not board or len(board[0]) == 0:
            return
        # Gets dimensions of board.
        m, n = len(board), len(board[0])
        print(m,n)
        # Iterate through the board and generate populated list!
        for i,row in enumerate(board):
            for j,ele in enumerate(row):
                #Sum of the element
                count = 0
                for r in range(max(0,i-1),min(m, i+2)):
                    for c in range(max(0,j-1), min(n, j+2)):
                        if (r,c) != (i,j) and (1 <= board[r][c] <= 2):
                            count += 1

                # Previously 0 element turned to be 1 is represented as 3 here. [Point 4]
                # Previously 1 element turned to 0 is represented as 2 here. [Point 2 or 3]
                # Processing that particular point!
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
                elif count < 2 or count > 3:
                    board[i][j] = 2
        
        # Final formatting
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0
        
        
