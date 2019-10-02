"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        maxVal = -float('inf')
        while stack:
            node, currDepth = stack.pop()
            children = node.children
            if not any(children):
                maxVal = max(maxVal, currDepth)
            for c in children:
                if c:
                    stack.append([c, currDepth+1])
        return maxVal
