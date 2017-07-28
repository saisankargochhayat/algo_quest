class disjoint_set():
    def __init__(self,a):
        self.a = a
        self.parents = [i for i in a]
        self.rep = [True for i in a]
        self.rank = [1 for i in a]
    def find_parent(self,i):
        current = i
        if current == parents[current]:
            return current
        else:
            parents[i] = self.find_parent(parents[current])
            return parents[i]
    def union(self,i,j):
        if i == j:
            return
        parent1 = self.find_parent(i)
        parent2 = self.find_parent(j)
        if parent1 == parent2:
            return
        if self.rank[parent1] > self.rank[parent2]:
            self.parents[parent2] = parent1
            self.rep[parent2] = False
            return
        if self.rank[parent2] > self.rank[parent1]:
            self.parents[parent1] = parent2
            self.rep[parent1] = False
            return
        self.parents[parent1] = parent2
        self.rank[parent2]+= 1
        self.rep[parent1] = False
        return
    def find_same_set(self,i,j):
        if i==j:
            return True
        parent1 = self.find_parent(i)
        parent2 = self.find_parent(j)
        if parent1 == parent2:
            return True
        else:
            return False
