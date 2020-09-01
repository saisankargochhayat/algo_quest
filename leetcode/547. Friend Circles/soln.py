from typing import List
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        print(M)
        u = UnionFind(len(M))
        # Lets find edges from this matrices 
        m, n = len(M), len(M[0])
        for i in range(m):
            for j in range(i):
                # Edge discovered
                if M[i][j]:
                    u.union(i, j)
        print(u.parent)
        res = set()
        for k in range(m):
            res.add(u.find(k))
        print(len(res))
                    

class UnionFind():
    def __init__(self, vertices: int):
        self.parent = [i for i in range(vertices)]
        self.size = [0 for i in range(vertices)]

    # Path compression 
    def _root(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        # Lets do path compression on these elements. 
        # x = self._root(x)
        # y = self._root(y)
        # We join the smaller weight tree to the larger one. 
        if self.size[x] < self.size[y]:
            self.parent[y] = x
            self.size[x] += 1
        else:
            self.parent[x] = y
            self.size[y] += 1
        x = self._root(x)
        y = self._root(y)
    
    # Find parent of x.
    def find(self, x: int) -> int:
        return self.parent[x]




s = Solution()
input = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
s.findCircleNum(input)