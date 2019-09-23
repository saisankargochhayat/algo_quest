class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        top, left, right, bottom = 0, 0, len(matrix[0])-1, len(matrix)-1
        soln = []
        direction = 0 
        # 0 -> right 1 -> down 2 -> left 3 -> up
        while (top <= bottom and left <= right):
            if direction == 0:
                # right
                for j in range(left,right+1):
                    soln.append(matrix[top][j])
                top += 1
                direction += 1
                #down
            elif direction == 1:
                for i in range(top, bottom+1):
                    soln.append(matrix[i][right])
                right -= 1
                direction += 1
            elif direction == 2:
                for j in range(right, left-1, -1):
                    soln.append(matrix[bottom][j])
                bottom -= 1
                direction += 1
            elif direction == 3:
                for i in range(bottom, top-1, -1):
                    soln.append(matrix[i][left])
                left += 1
                direction += 1
            direction %= 4
        return soln
