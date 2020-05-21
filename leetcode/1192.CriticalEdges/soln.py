from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfsUtil(u, time):
            # We encounter this here first. 
            visited[u] = True
            # Initialize low and disc.
            disc[u] = time
            low[u] = time
            time += 1

            # Now let's recurse for all its adjacent nodes. 
            for v in graph[u]:
                # if v not encountered make it a child in dfs tree and recurse.
                if visited[v] == False:
                    parent[v] = u 
                    dfsUtil(v, time)

                    # Check if the subtree rooted with v has a connection to 
                    # one of the ancestors of u 
                    low[u] = min(low[u], low[v])   
                    ''' If the lowest vertex reachable from subtree 
                    under v is below u in DFS tree, then u-v is 
                    a bridge'''
                    if low[v] > disc[u]: 
                        res.append([u,v])
                # if v is not a parent of u then we update lower value. 
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])

            
        
        # We convert to a directed graph.
        graph = defaultdict(list)
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        res = []
        
        # Now lets start 
        visited = [False] * n
        low = [float("inf") for i in range(n)]
        disc = [float("inf") for i in range(n)]
        parent = [-1] * n 
        time = 0 
        for i in range(n):
            if visited[i] == False:
                dfsUtil(i, time)
        return res