from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        # Adding as v, w tuple to a source.
        for edge in times:
            graph[edge[0]].append((edge[1], edge[2]))
        visited = set()
        distanceArray = [float("inf")]*N
        # Distance of source
        distanceArray[K-1] = 0
        heap = [(0,K)]
        # Till elements are accesible
        while heap:
            weight, u = heapq.heappop(heap)
            if u in visited: continue
            visited.add(u)
            for v,w in graph[u]:
                if v in visited: continue
                if distanceArray[v-1] > (distanceArray[u-1]+w):
                    distanceArray[v-1] = distanceArray[u-1]+w
                heapq.heappush(heap, (distanceArray[v-1], v))
            
        # print(distanceArray)
        maxLen = max(distanceArray)
        return -1 if maxLen == float("inf") else maxLen
