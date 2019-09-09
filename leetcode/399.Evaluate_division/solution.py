from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            eq = equations[i]
            graph[eq[0]].append((eq[1], values[i]))
            graph[eq[1]].append((eq[0], 1/values[i]))
        soln = []
        for q in queries:
            value = self.findPath(q[0], q[1], graph, set(), 1.0)
            soln.append(value)
        return soln
    
    def findPath(self, start, end, graph, visited, value):
        # Ignores start if visited already.
        if start not in graph or end not in graph or start in visited:
            return -1.0
        # takes care care of end of recursion and the edge to itself case.
        if start == end:
            return value
        visited.add(start)
        for i in range(len(graph[start])):
            tmp = self.findPath(graph[start][i][0], end, graph, visited, value*graph[start][i][1])
            if tmp != -1.0:
                return tmp
        return -1.0
        
            
            
        
