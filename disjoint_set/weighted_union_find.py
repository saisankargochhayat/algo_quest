# Goal is to implemented weighted union find with path compression.
class UnionFind:
    def __init__(self, N):
        # Stores the set it belongs to.
        self.parent = [i for i in range(N)]
        # Stores the size of set, needed for weighted union.
        self.size = [1 for i in range(N)]

    def _root(self, i):
        # The idea is to set the root of i to its grandparent, hence compressing the path.
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def find(self, x):
        # find the parent set of the element.
        return self._root(x)

    def union(self, x, y):
        # find the union of two dsijoint sets given.
        x_root = self._root(x)
        y_root = self._root(y)
        
        # this the weighted union step.
        if self.size[x_root] < self.size[y_root]:
            # add x to y tree.
            self.parent[x_root] = self.parent[y_root]
            self.size[y_root] += self.size[x_root]
        else:
            # add y to x tree.
            self.parent[y_root] = self.parent[x_root]
            self.size[x_root] += self.size[y_root]

u = UnionFind(10)
connections = [(0, 1), (1, 2), (0, 9), (5, 6), (6, 4), (5, 9)]
# union
for i, j in connections:
    u.union(i, j)

# find
for i in range(10):
    print('item', i, '-> component', u.find(i))
        
        