class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        from collections import defaultdict
        graph = defaultdict(set)
        for x, y in dislikes:
            graph[x].add(y)
            graph[y].add(x)
        # Bipartiion check
        color = {}
        seen = set()
        def dfsHelper(node, c=0):
            # Check if existing color is same as attempted. Not recurse that number again. 
            if node in color:
                return color[node] == c
            color[node] = c
            # Now recurse for all child nodes. 
            # After changing to a different color. 
            # All operator gives true if everything is true. 
            return all(dfsHelper(nei, c^1) for nei in graph[node])
        
        return all(dfsHelper(node) for node in range(1, N+1) if node not in color)
    
