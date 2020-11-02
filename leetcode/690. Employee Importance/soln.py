"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        e, res = {}, 0
        for emp in employees:
            i, points, subs = emp.id, emp.importance, emp.subordinates
            e[i] = [points, subs]
        
        # this is a bfs search
        queue = [e.get(id)]
        while queue:
            newQueue = []
            for i in queue:
                res += i[0]
                subOrds = [e.get(k) for k in i[1]]
                newQueue.extend(subOrds)
            queue = newQueue
                
        return res
