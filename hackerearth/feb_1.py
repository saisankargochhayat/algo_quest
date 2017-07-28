import random
class graph:
    def __init__(self):
        self.vertices = {}
    def add_node(self,myid):
        if myid in self.vertices:
            print("Node already added")
        else:
            self.vertices[myid] = set()
    def add_edge(self,id1,id2):
        self.vertices[id1].add(id2)
    def show_graph(self):
        for key in self.vertices:
            print(str(key)+" : " + str(self.vertices[key]))
    def dfs(self,root):
        maxi = 0
        stack = [root]
        visited = set()
        seq = []
        while stack:
            curr = stack.pop()
            if int(curr/3) > maxi:
                maxi = int(curr/3)
            if curr not in visited:
                seq.append(curr)
                visited.add(curr)
                stack.extend(self.vertices[curr] - visited)
        return maxi
    def bfs(self,root):
        queue = [root]
        visited = set()
        seq = []
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                seq.append(curr)
                visited.add(curr)
                queue.extend(self.vertices[curr] - visited)
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
            for adj in adjs:
                if colors[adj]!=-1 and colors[adj]!=new_color:
                    return False
                else:
                    colors[adj] = new_color
            queue.extend(adjs - visited)

def check_exist(i,j,n,road):
    if j<0 or j>2:
        return False
    if i<0 or i>n-1:
        return False
    if road[i][j]==1:
        return False
    return True
t = int(input())
def check_all_blocked(a):
    if a[0]==1 and a[1]==1 and a[2]==1:
        return True
    else:
        return False
for i in range(t):
    n,q = input().split(' ')
    n = int(n)
    q = int(q)
    road = [[0,0,0] for k in range(n)]
    for j in range(q):
        x,y = input().split(' ')
        x = int(x)
        y = int(y)
        road[x-1][y-1]=1
    g = graph()
    for j in range(n):
        for k in range(3):
            if road[j][k]==0:
                g.add_node(j*3 + k)
                if check_exist(j+1,1,n,road):
                    g.add_edge(j*3+k,(j+1)*3+1)
                else:
                    for new in [k-1,k,k+1]:
                        if check_exist(j+1,new,n,road):
                            g.add_edge(j*3+k,(j+1)*3+new)
    maxi = g.dfs(0)
    one = g.dfs(1)
    two = g.dfs(2)
    if maxi < one:
        maxi = one
    if maxi < two:
        maxi = two
    print(maxi+1)
