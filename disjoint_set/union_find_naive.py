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


u = UnionFind(10)
connections = [(0, 1), (1, 2), (0, 9), (5, 6), (6, 4), (5, 9)]
# union
for i, j in connections:
    u.union(i, j)

# find
for i in range(10):
    print('item', i, '-> component', u.find(i))