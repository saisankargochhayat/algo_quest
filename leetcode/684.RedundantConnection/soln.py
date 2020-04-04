class UnionFind:
    def __init__(self, n):
        self.graph = [i for i in range(n+1)]
    
    def find(self, x):
        while x != self.graph[x]:
            # path compression
            self.graph[x] = self.graph[self.graph[x]]
            x = self.graph[x]
        return x
    
    def union(self, x, y):
        # join y to x
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            self.graph[xp] = yp

    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        l = len(edges)
        uf = UnionFind(l)
        for edge in edges:
            x, y = uf.find(edge[0]), uf.find(edge[1])
            if x != y:
                # not a cycle
                uf.union(edge[0], edge[1])
            else:
                return edge


# class UnionFind:
#     def __init__(self, N):
#         # Stores the set it belongs to.
#         self.arr = [i for i in range(N)]
#         # Stores the size of set, needed for weighted union.
#         self.size = [1 for i in range(N)]

#     def _root(self, i):
#         # The idea is to set the root of i to its grandparent, hence compressing the path.
#         while self.arr[i] != i:
#             self.arr[i] = self.arr[self.arr[i]]
#             i = self.arr[i]
#         return i

#     def find(self, x):
#         # find the parent set of the element.
#         return self._root(x)

#     def union(self, x, y):
#         # find the union of two dsijoint sets given.
#         x_root = self._root(x)
#         y_root = self._root(y)
        
#         # this the weighted union step.
#         if self.size[x_root] < self.size[y_root]:
#             # add x to y tree.
#             self.arr[x_root] = self.arr[y_root]
#             self.size[y_root] += self.size[x_root]
#         else:
#             # add y to x tree.
#             self.arr[y_root] = self.arr[x_root]
#             self.size[x_root] += self.size[y_root]
                
