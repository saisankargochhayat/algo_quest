# https://github.com/tangothu/Python-Leetcode/blob/master/removeObstacle.py
# BFS for undirected, unweighted graph shortest path
def removeObstacle(numRows, numColumns, lot):
    """
    See shortestMazePath for more info. This is similar to shortestMazePath with
    slightly different conditions.
    1 <= numRows, numColumns <= 1000
    """
    possible_paths = {
        'left': [-1, 0],
        'right': [1, 0],
        'up': [0, 1],
        'down': [0, -1]
    }
    numRows, numColumns, dist = len(lot), len(lot[0]), 0
    queue = [(0, 0, lot[0][0])] # (x, y, val)
    visited = set() # Points already explored
    while queue:
        next = []
        for x, y, val in queue:
            if val == 9:
                return dist
            if (x,y) not in visited:
                for x1, y1 in possible_paths.values():
                    nextX, nextY = x + x1, y + y1
                    if 0 <= nextX < numRows and 0 <= nextY < numColumns:
                        next.append((nextX, nextY, lot[nextX][nextY]))
                visited.add((x,y))
        queue = next
        dist += 1
    return -1
    





if __name__ == '__main__':
    lot = [
            [1,0,0],
            [1,0,0],
            [1,9,1]
            ]
    numRows = len(lot)
    numColumns = len(lot[0])
    # print(removeObstacle(numRows, numColumns, lot))
    assert removeObstacle(numRows, numColumns, lot) == 3

    lot = [
            [1,1,1,1],
            [0,1,1,1],
            [0,1,0,1],
            [1,1,9,1],
            [0,0,1,1]
            ]
    numRows = len(lot)
    numColumns = len(lot[0])
    # print(removeObstacle(numRows, numColumns, lot))
    assert removeObstacle(numRows, numColumns, lot) == 5
