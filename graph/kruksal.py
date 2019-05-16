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

import random
class graph:
    def __init__(self):
        self.vertices = {}
    def add_node(self,myid):
        if myid in self.vertices:
            print("Node already added")
        else:
            self.vertices[myid] = set()
    def add_edge(self,id1,id2,weight):
        self.vertices[id1].add((id2,weight))
        self.vertices[id2].add((id1,weight))
    def show_graph(self):
        for key in self.vertices:
            print(str(key)+" : " + str(self.vertices[key]))
    def dfs(self,root):
        stack = [root]
        visited = set()
        seq = []
        while stack:
            curr = stack.pop()
            if curr not in visited:
                seq.append(curr)
                visited.add(curr)
                stack.extend(self.vertices[curr][0] - visited)
        return seq
    def bfs(self,root):
        queue = [root]
        visited = set()
        seq = []
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                seq.append(curr)
                visited.add(curr)
                queue.extend(self.vertices[curr][0] - visited)
        return seq
    def check_bipartite(self):
        all_vertices = self.vertices.keys()
        root = random.choice(list(all_vertices))
        colors = {}
        for key in all_vertices:
            colors[key] = -1
        colors[root] = 0
        queue = [root]
        visited = set()
        while queue:
            curr = queue.pop(0)
            curr_color = colors[curr]
            new_color = (curr_color+1)%2
            adjs = self.vertices[curr]
            visited.add(curr)
            for adj,weight in adjs:
                if colors[adj]!=-1 and colors[adj]!=new_color:
                    return False
                else:
                    colors[adj] = new_color
                if adj not in visited:
                    queue.append(adj)
        return True

    # def kruskal():
    #     mst = set()
    #     d = disjoint_set()
    #     for v in self.vertices:
    #         d.add_node(v)
    #     edges
