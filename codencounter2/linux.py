from collections import deque
import heapq
class package(object):
    def __init__(self,name,priority):
        self.priority = priority
        self.name = name
    def getName(self):
        return self.name
    def getPriority(self):
        return self.priority
    def __lt__(self,other):
        if self.priority < other.priority:
            return True
        if self.priority > other.priority:
            return False
        if self.name < other.name:
            return True
        return False

def kahn_topsort(graph):
    in_degree = {u: 0 for u in graph}    
    for u in graph:                          
        for v in graph[u]:
            in_degree[v] += 1
    packages = {u : package(u,in_degree[u]) for u in graph}
    Q = []               
    for u in in_degree:
        if in_degree[u] == 0:
            heapq.heappush(Q,packages[u])
    L = []     
    while len(Q) > 0:
        obj = heapq.heappop(Q)         
        u = obj.name
        L.append(u)         
        for v in graph[u]:
            in_degree[v] -= 1
            packages[v].priority = in_degree[v]
            if in_degree[v] == 0:
                heapq.heappush(Q,packages[v])
    if len(L) == len(graph):
        return L
    else:                    
        return []            


def main():
    graph_tasks = {}
    n, m = input().split()
    n, m = [int(n), int(m)]
    for i in range(m):
        y,x = input().strip().split()
        if x in graph_tasks:
            graph_tasks[x].append(y)
        else:
            graph_tasks[x] = [y]
        if y not in graph_tasks:
            graph_tasks[y] = []
    order = kahn_topsort(graph_tasks)
    print(' -> '.join(order))


main()
