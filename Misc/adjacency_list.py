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
print(adjList)
for i in range(len(edge_u)):
    u=edge_u[i]
    v=edge_v[i]
    adjList[u].append(v)

print(adjList)
