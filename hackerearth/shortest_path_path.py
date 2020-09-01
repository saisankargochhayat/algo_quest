# https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/shortest-path-revisited-9e1091ea/
# https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
import heapq
from collections import defaultdict

# Graph is stored here. 
graph = defaultdict(list)

# Stores path from start node to all other nodes, initialized to inf initially. 
res = {}

def shortest_path(start_node):
    seen = set()
    heap = []
    res[start_node] = (0, 0, None) 
    heapq.heappush(heap, (0, start_node))
    while heap:
        # Lets check nodes of this node.
        currVal, v = heapq.heappop(heap)
        if v not in seen:
            for neighbour, value in graph[v]:
                if currVal + value < res[neighbour][0]:
                    # Path weight, edge weight, parent node
                    res[neighbour] = (currVal + value, value, v)
                    heapq.heappush(heap, (currVal+value, neighbour))    
        seen.add(v)

# finds path from every node to start_node if possible. 
def findPath(res, start_node):
    paths = defaultdict(list)
    for node in res.keys():
        curr_node, edge_val, parent = res[node]
        while parent != None:
            paths[node].append(edge_val)
            _, edge_val, parent = res[parent]
    return paths


if __name__ == "__main__":
    # n = vertices, m = edges
    n, m, free_tickets = map(int, input().split())
    for i in range(m):
        try:
            a, b, value = map(int, input().split())
            graph[a].append((b, value))
            graph[b].append((a, value))
        except:
            break
    # We also store (distance from source, parent)
    res = {k:(float('inf'), None, None) for k in range(1, n+1)}
    shortest_path(1)
    paths = findPath(res, start_node=1)
    ans = list(paths.values())
    print(ans)
    # Reverse this path arrays 
    new_ans = [sorted(arr, reverse=True) for arr in ans]
    print(new_ans)
    # ans = list(res.values())
    # del ans[0]
    # print(*ans)
# print(graph)
print(res)


