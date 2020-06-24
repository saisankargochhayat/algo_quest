# Will be solving it with Kahn algorithm
# Bascially maintain in-degree array, and do topological sort. 
# Remove an element with in-degree and reduce in-deg of adj nodes. 
# Length of topo-sort == number of vertices in graph return
# Else there is a cycle in the graph. 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        topOrder = []
        
        for x,y in prerequisites:
            graph[x].append(y)
            in_degree[y] += 1
        
        # Find all nodes having in-degree to be zero. 
        queue = deque([index for index, deg in enumerate(in_degree) if deg == 0])
        # print(queue, graph, in_degree)
        count = 0
        while queue:
            # We remove element with in-degree 0 and append to topOrder
            node = queue.popleft()
            topOrder.append(node)
            # We reduce edge in-deg by 1 and if it hits 0, we add to queue.
            for edge in graph[node]:
                in_degree[edge] -= 1
                if in_degree[edge] == 0:
                    queue.append(edge)
            count += 1
        return [] if count != numCourses else topOrder[::-1]
        
        
