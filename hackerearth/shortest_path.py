# https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms
# https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
import heapq
from collections import defaultdict

# Graph is stored here. 
graph = defaultdict(list)

# Stores path from start node to all other nodes, initialized to inf initially. 
res = defaultdict(int)

def shortest_path(start_node):
    seen = set()
    heap = []
    res[start_node] = 0 
    heapq.heappush(heap, (res[start_node], start_node))
    while heap:
        # Lets check nodes of this node.
        currVal, v = heapq.heappop(heap)
        if v not in seen:
            for neighbour, value in graph[v]:
                if currVal + value < res[neighbour]:
                    res[neighbour] = currVal + value
                    heapq.heappush(heap, (currVal+value, neighbour))    
        seen.add(v)

if __name__ == "__main__":
    # n = vertices, m = edges
    n, m = map(int, input().split())
    for i in range(m):
        try:
            a, b, value = map(int, input().split())
            graph[a].append((b, value))
            graph[b].append((a, value))
        except:
            break
    res = {k:float('inf') for k in range(1, n+1)}
    shortest_path(1)
    # ans = list(res.values())
    # del ans[0]
    # print(*ans)
print(graph)
print(res)


