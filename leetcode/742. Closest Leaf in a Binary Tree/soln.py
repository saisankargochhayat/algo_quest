# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The idea is to generate a graph out of a binary tree and then do a BFS on that graph to find the nearest leafnode. 

class Solution:
    def findClosestLeaf(self, root, k):
        # Write your code here
        from collections import defaultdict
        from collections import deque
        graph = defaultdict(list)
        leafNode = set()
        # Lets convert the binary tree into a graph and also store when we encounter an leaf node. 
        self.convertToGraph(root, graph, leafNode)
        # Now that we have the populated graph, lets do a bfs on it to find nearest leaf. 
        def bfs(graph, k):
            queue = [k]
            seen = set()
            while queue:
                neighbours = []
                for node in queue:   
                    # Nearest leafNode found
                    if node in leafNode:
                        return node
                    if node not in seen:
                        neighbours.extend(graph[node])
                        seen.add(node)
                queue = neighbours
        res = bfs(graph, k)
        return res


    def convertToGraph(self, root, graph, leafNode):
        if root:
            # Generate graph connections and recurse below.
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                self.convertToGraph(root.left, graph, leafNode)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                self.convertToGraph(root.right, graph, leafNode)
            # Capture leaf node values here
            if root.left == None and root.right == None:
                leafNode.add(root.val)
