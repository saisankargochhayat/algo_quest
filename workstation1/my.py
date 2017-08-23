import heapq
class node(object):
    def __init__(self,name):
        self.priority = float('inf')
        self.name = name
    def __lt__(self,other):
        if self.priority < other.priority:
            return True
        return False
class graph:
    def __init__(self):
        self.vertices = {}
        self.depth = {}
        self.nodes = {}
    def add_node(self,myid):
        self.vertices[myid] = set()
        self.depth[myid] = 0
        self.nodes[myid] = node(myid)
    def add_edge(self,id1,id2,weight):
        self.vertices[id1].add((id2,weight))
        self.vertices[id2].add((id1,weight))
    def bfs(self,root):
        queue = []
        self.nodes[root].priority = 0
        self.depth[root] = 0
        heapq.heappush(queue,self.nodes[root])
        visited = set()
        seq = []
        while queue:
            mynode = heapq.heappop(queue)
            curr = mynode.name
            if curr not in visited:
                seq.append(curr)
                visited.add(curr)
                for v in self.vertices[curr]:
                    if v[0] not in visited:
                        self.nodes[v[0]].priority = self.nodes[curr].priority + v[1]
                        self.depth[v[0]] = self.depth[curr] + v[1]
                        heapq.heappush(queue,self.nodes[v[0]])
        return seq

M = 10**9 + 7
g = graph()
n,start = list(map(int,input().strip().split()))
start = start
for i in range(n):
    g.add_node(i+1)
while(True):
    k = input()
    if k == '0':
        break
    x,y,w = list(map(int,k.strip().split()))
    g.add_edge(x,y,w)
solution = [str(k) for k in g.bfs(start)]
print(' '.join(solution))
mysum = 0
for k in g.depth:
    mysum += g.depth[k]
    mysum = mysum%M
print(mysum)
