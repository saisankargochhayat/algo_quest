# A utility function to find the distance between two points
def dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

# O(N) operation as at most 3 points are passed to this. 
def brute(xP, n):
    minDis = float("inf")
    for i in range(n): 
        for j in range(i + 1, n): 
            currDis = dist(xP[i], xP[j])
            if currDis < minDis: 
                minDis = currDis
    return minDis 


def stripClosest(strip, size, d):
    minVal = d
    # Pick all points one by one and  
    # try the next points till the difference  
    # between y coordinates is smaller than d.  
    # This is a proven fact that this loop 
    # runs at most 6 times  
    for i in range(size): 
        j = i + 1
        while j < size and (strip[j][1] - 
                            strip[i][1]) < minVal: 
            minVal = dist(strip[i], strip[j]) 
            j += 1
  
    return minVal  



def closestDivide(P, Q, n):
    if n <= 3:
        return brute(P, n)
    # Divide at middle
    mid = n//2
    midPoint = P[mid]

    lQ, rQ = [], [] # All points left of mid and right of mid, sorted vertically. 
    for p in Q:
        if p[0] < midPoint[0]:
            lQ.append(p)
        else:
            rQ.append(p)

    # Lets divide at mid point
    dl = closestDivide(P[:mid], lQ, mid)
    dr = closestDivide(P[mid:], rQ, n-mid)

    d = min(dl, dr) # Min of both these sides. 

    # Build strip that contains the points close to Y. In the partial list. 
    strip = []
    for point in Q:
        if abs(point[0] - midPoint[0]) < d:
            strip.append(point)
    
    # Find the closest points in strip.  
    # Return the minimum of d and closest  
    # distance is strip[]  
    return min(d, stripClosest(strip, len(strip), d)) 



def closestSquaredDistance(numRobots, positionX, positionY):
    points = list(zip(positionX, positionY))
    x_sorted = sorted(points, key=lambda x:x[0])
    y_sorted = sorted(points, key=lambda x:x[1])
    # print(points, x_sorted, y_sorted)
    ans = closestDivide(x_sorted, y_sorted, numRobots)
    return ans





# O(n^2)
# def closestSquaredDistance(numRobots, positionX, positionY):
#     minDis = float("inf")
#     for i in range(numRobots):
#         for j in range(i+1, numRobots):
#             curr_dist = (positionX[i] - positionX[j])**2 + (positionY[i] - positionY[j])**2
#             minDis = min(curr_dist, minDis)
#     return minDis



print(closestSquaredDistance(4, [77, 1000, 992, 1000000], [0, 1000, 500, 0]))
print(closestSquaredDistance(6, [2,12,40,5,12,3], [3,30,50,1,10,4]))
print(closestSquaredDistance(3, [0,10,15], [0,10,20]))