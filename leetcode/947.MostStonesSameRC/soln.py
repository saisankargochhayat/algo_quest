# Idea is to find MST. 
# This is a weighted path compression union find implementation.
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

class UnionFind:    
    def __init__(self, n):
        # Every element is a different component.
        self.data = [i for i in range(n)]
    
    def find(self, i):
        if i != self.data[i]:
            self.data[i] = self.find(self.data[i])
        return self.data[i]
    
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.data[pi] = pj


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        l = len(stones)
        # Double size so that col and rows wont overlap.
        dsu = UnionFind(20000)
        # Now we do an union, row to col 
        for x,y in stones:
            dsu.union(x, y+10000)
        # Now we find number of unique components 
        u = len({dsu.find(x) for x, y in stones})
        # result is total number of nodes - unique components
        return l - u

        
