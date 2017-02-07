class disjoint_set:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
        self.count = {}
    def add_node(self,key):
        self.parents[key] = key
        self.ranks[key] = 0
        self.count[key] = 1
    def make_child(self,child,parent):
        self.parents[child] = parent
    def find_parent(self,child):
        if self.parents[child] == child:
            return child
        else:
            p = self.find_parent(self.parents[child])
            self.parents[child] = p
            return p
    def check_same_set(self,child1,child2):
        parent1 = self.find_parent(child1)
        parent2 = self.find_parent(child2)
        if parent1 == parent2:
            return True
        else:
            return False
    def union_set(self,child1,child2):
        parent1 = self.find_parent(child1)
        parent2 = self.find_parent(child2)
        if parent1 != parent2:
            if self.ranks[parent1] > self.ranks[parent2]:
                self.make_child(parent2,parent1)
                self.count[parent1] = self.count[parent1] + self.count[parent2]
            elif self.ranks[parent2] > self.ranks[parent1]:
                self.make_child(parent1,parent2)
                self.count[parent2] = self.count[parent1] + self.count[parent2]
            else:
                self.make_child(parent1,parent2)
                self.ranks[parent2] = self.ranks[parent2]+1
                self.count[parent2] = self.count[parent1] + self.count[parent2]
    def get_all_set_members(self,child):
        members = []
        main_parent = self.find_parent(child)
        for curr in self.parents:
            p = self.find_parent(curr)
            if p == main_parent:
                members.append(curr)
        return members
    def count_members(self,child):
        parent = self.find_parent(child)
        return self.count[parent]
d = disjoint_set()
d.add_node(1)
d.add_node(2)
d.add_node(3)
d.add_node(4)
d.add_node(5)
d.add_node(6)
d.add_node(7)
d.add_node(8)
d.union_set(1,3)
d.union_set(5,7)
d.union_set(1,7)
d.union_set(2,4)
d.union_set(6,8)
d.union_set(2,6)
print(d.count_members(2))
