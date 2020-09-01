class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position is in the center
        x = y = 0
        # facing north
        idx = 0
        
        for i in instructions:
            if i == "L":
                idx = (idx + 3) % 4
            elif i == "R":
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]
        
        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        return (x == 0 and y == 0) or idx != 0

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, deg = 0, 0, 90
        for char in instructions:
            # calc direction and mod to stay within 360.
            if char == "L":
                deg += 90
                deg = deg % 360
            if char == "R":
                deg -= 90
                deg = deg % 360
            # calc movement based on direction
            if char == "G":
                if deg == 0 or deg/360 == 1:
                    x, y = x, y+1
                elif deg / 90 == 1:
                    x, y = x+1, y
                elif deg / 90 == 2:
                    x, y = x, y-1
                elif deg / 90 == 3:
                    x, y = x-1, y
        return (x-0)**2+(y-0)**2 == 0 or deg != 90
