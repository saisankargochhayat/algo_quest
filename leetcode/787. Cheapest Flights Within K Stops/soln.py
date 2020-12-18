# This is BFS with a Priority Queue instead of a Normal Queue and also 
# we dont maintain seen as we want to explore another route and its directed and without cycles. 
# The most cost efficient routes are explored first but if they exceed k stop they are discarded. 
from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))
        
        pqueue = [(0, src, K+1)]  # stops = k edges = k+1
        while pqueue:
            cost, i, t = heappop(pqueue)  # i = current node
            if i == dst:
                return cost
            # Else we start exploring neighbours
            for v, c in graph[i]:
                if t > 0:
                    heappush(pqueue, (cost+c, v, t-1))
            
        
        return -1 # incase we didn't find destination with the given conditions. 






# Dijkstra doesnt work as it eliminates more expensive shorter paths. 
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
#         graph = defaultdict(list)
#         for u, v, cost in flights:
#             graph[u].append((v, cost))
        
#         seen = set()
#         costDict = {k:float("inf") for k in range(n)}
#         costDict[src] = 0  # distance from source to source is always 0. 
        
#         queue = [(src, 0)]
#         while queue:
#             cNode, t = heappop(queue) # t is the distance
#             cNodeCost = costDict[cNode]
#             for v, cost in graph[cNode]: # we explore adj nodes of this node 
#                 if v in seen:
#                     continue
#                 if t + 1 <= K+1:
#                     if cost + cNodeCost < costDict[v]: # Cheaper route found
#                         costDict[v] = cost + cNodeCost
#                     heappush(queue, (v, t+1))
#             print(cNode, costDict)
#             seen.add(cNode)
                        
#         print(graph, costDict)    
#         return costDict[dst] if costDict[dst] != float('inf') else -1
