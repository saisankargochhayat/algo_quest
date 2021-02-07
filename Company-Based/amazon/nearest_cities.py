# link - https://aonecode.com/amazon-online-assessment-nearest-cities
from typing import List
from collections import defaultdict
def findEuclidean(x1, x2, y1, y2) -> int:
    return (abs(x1-x2)**2) + (abs(y1-y2)**2)
def findNearestCities(numOfPoints: int, points: List[str], xCoordinates: List[int], yCoordinates: List[int],
                      numOfQueries: int, queries: List[str]) -> List[str]:
    xMap = defaultdict(list)
    yMap = defaultdict(list)
    pointMap = dict()
    for i in range(numOfPoints):
        pointMap[points[i]] = (xCoordinates[i], yCoordinates[i])
        xMap[xCoordinates[i]].append((yCoordinates[i], points[i]))
        yMap[yCoordinates[i]].append((xCoordinates[i], points[i]))
    ans = []
    # Now we have the maps we can use in our queries. 
    for j in range(numOfQueries):
        qPoint = queries[j]
        x1, y1 = pointMap[qPoint]
        res = [] # would have tuples of (dist, point_name)
        # Close points in xMap 
        xList, yList = xMap.get(x1),  yMap.get(y1)
        # Calc for points where x coordinate matches
        for y2, targetPoint in xList:
            if targetPoint != qPoint:
                cDist = findEuclidean(x1, x1, y1, y2)
                res.append((cDist, targetPoint))
        for x2, targetPoint in yList:
            if targetPoint != qPoint:
                cDist = findEuclidean(x1, x2, y1, y1)
                res.append((cDist, targetPoint))
        if res:
            ans.append(sorted(res)[0][1])
        else:
            ans.append(None)
    return ans
    


n = 3
points = ["p1","p2","p3"]
xCoordinates = [30, 20, 10]
yCoordinates = [30, 20, 30]
numOfQueriedPoints = 3
queriedPoints = ["p3", "p2", "p1"]

# n = 5
# points =  ["p1", "p2","p3", "p4", "p5"]
# xCoordinates = [10, 20, 30, 40, 50] 
# yCoordinates =  [10, 20, 30, 40, 50]
# numOfQueriedPoints = 5  
# queriedPoints = ["p1", "p2", "p3", "p4", "p5"]

print(findNearestCities(n, points, xCoordinates, yCoordinates, numOfQueriedPoints, queriedPoints))