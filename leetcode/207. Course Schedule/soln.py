# Solution is basically finding cycle in a directed graph. 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        graph = defaultdict(list)
        for x,y in prerequisites:
            graph[x].append(y)
        
        # rStack = recursion stack
        def dfs(n, visited, rStack):
            visited[n] = True
            rStack[n] = True
            for child in graph[n]:
                if not visited[child]:
                    if dfs(child, visited, rStack) == True:
                        return True
                elif rStack[child] == True:
                    return True                    
            # Reset the recurse stack as we go back. 
            rStack[n] = False
            return False
        
        
        # Driver code. 
        visited = [False] * numCourses
        rStack = [False] * numCourses
        for node in list(graph.keys()):
            if visited[node] == False:
                # If cycle exists we return false.
                if dfs(node, visited, rStack) is True:
                    return False
        # No cycle exists. 
        return True
