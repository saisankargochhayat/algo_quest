def findMinDistance(w, h, n):
    import itertools
    from collections import deque
    height, width = h, w
    arr = []
    for i in range(height):
        for j in range(width):
            arr.append((i,j,0))

    ans = float("inf")
    print([pnt for pnt in itertools.combinations(arr,n)])
    for pnts in itertools.combinations(arr,n):
        q = deque([])
        visited = set()
        for m, n, dist in pnts:
            q.append((m,n,dist))
            visited.add((m,n))
        resAns = 0
        while q:
            i, j, dist = q.popleft()
            resAns = max(dist, resAns)
            for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0<=x<height and 0<=y<width and (x,y) not in visited:
                    q.append((x,y,dist+1))
                    visited.add((x,y))
        ans = min(resAns, ans)

    return ans


print(findMinDistance(5,1,1))

# print(findMinDistance(2,3,2))