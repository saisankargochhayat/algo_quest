#no of edges
n=int(input())
e=int(input())
edge_u=list()
edge_v=list()
for i in range(e):
    x,y=map(int,input().split())
    edge_u.append(x)
    edge_v.append(y)

# create empty adjacency lists - one for each node -
# with a Python list comprehension
adjList = [[] for k in range(n)]

for i in range(len(edge_u)):
    u=edge_u[i]
    v=edge_v[i]
    adjList[u].append(v)
    adjList[v].append(u)

# for i in range(len(edge_v)):
#     u=edge_u[i]
#     v=edge_v[i]
#     adjList[v].append(u)

print(adjList)


def dfs(graph, start):
    visited=[False for k in range(n)]
    stack=[start]
    visited[start]=True
    order=list()
    while stack:
        vertex=stack.pop()
        order.append(vertex)
        for i in graph[vertex]:
            if not visited[i]:
                stack.append(i)
                visited[i]=True
    return order

print(dfs(adjList,0))
