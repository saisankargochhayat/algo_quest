class graph:
    def __init__(self):
        self.vertices = {}
        self.depth = {}
    def add_node(self,myid):
        if myid in self.vertices:
            print("Node already added")
        else:
            self.vertices[myid] = set()
            self.depth[myid] = 0
    def add_edge(self,id1,id2):
        self.vertices[id1].add(id2)
        self.vertices[id2].add(id1)
    def show_graph(self):
        for key in self.vertices:
            print(str(key)+" : " + str(self.vertices[key]))
    def bfs(self,root):
        queue = [root]
        visited = set()
        seq = []
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                # print('next Element is '+str(curr))
                seq.append(curr)
                visited.add(curr)
                # print(self.vertices[curr])
                # print(visited)
                for k in self.vertices[curr] - visited:
                    if k not in queue:
                        queue.append(k)
                        self.depth[k] = self.depth[curr]+1
                # print(queue)
        return seq

#no of edges
m,n=map(int,input().split())
x,y=map(int,input().split())
x = x-1
y = y-1
adjMatrix = [[0 for i in range(m)] for k in range(m)]

def checkValid(i,j):
    if i < 0 or i >= m:
        return False
    if j < 0 or j >= n:
        return False
    if adjMatrix[i][j] == 'T':
        return True
    else:
        return False
def getId(i,j):
    return n*i + j

g = graph()
# print(adjMatrix)
for i in range(m):
    adjMatrix[i]=input().split()
for i in range(m):
    for j in range(n):
        if adjMatrix[i][j] == 'T':
            g.add_node(getId(i,j))
for i in range(m):
    for j in range(n):
        if adjMatrix[i][j] == 'T':
            #check nw
            if checkValid(i-1,j-1):
                g.add_edge(getId(i,j),getId(i-1,j-1))
            #check n
            if checkValid(i-1,j):
                g.add_edge(getId(i,j),getId(i-1,j))
            #check ne
            if checkValid(i-1,j+1):
                g.add_edge(getId(i,j),getId(i-1,j+1))
            #check e
            if checkValid(i,j+1):
                g.add_edge(getId(i,j),getId(i,j+1))
            #check se
            if checkValid(i+1,j+1):
                g.add_edge(getId(i,j),getId(i+1,j+1))
            #check s
            if checkValid(i+1,j):
                g.add_edge(getId(i,j),getId(i+1,j))
            #check sw
            if checkValid(i+1,j-1):
                g.add_edge(getId(i,j),getId(i+1,j-1))
            #check e
            if checkValid(i,j-1):
                g.add_edge(getId(i,j),getId(i,j-1))

# print(g.vertices)
# print(getId(x,y))
g.bfs(getId(x,y))
# print(g.depth)
print(g.depth[max(g.depth)]+1)