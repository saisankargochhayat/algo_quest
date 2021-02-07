"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def deepCopy(node):
            if not node:
                return
            # If node is already visited before return node.
            # Return cloned node.
            if node in visited:
                return visited[node]
            
            # Create a new node 
            newNode = Node(node.val, [])
            visited[node] = newNode
            newNode.neighbors = [deepCopy(n) for n in node.neighbors]
            
            return newNode
        
        return deepCopy(node)



class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        visited = set()
        graphMap = {}
        def deepCopy(parent, node, newNode):
            if node.val in visited:
                gNode = graphMap[node.val]
                parentSet = set([n.val for n in gNode.neighbors])
                if parent.val not in parentSet:
                    gNode.neighbors.append(parent)
                return gNode
            newNode.val = node.val
            visited.add(node.val)
            graphMap[node.val] = newNode
            newNeighbors = []
            for n in node.neighbors:
                newN = deepCopy(newNode, n, Node(-1))
                if newN:
                    newNeighbors.append(newN)
            newNode.neighbors = newNeighbors
            
            return newNode
        ans = deepCopy(Node(-1), node, Node())
        return ans