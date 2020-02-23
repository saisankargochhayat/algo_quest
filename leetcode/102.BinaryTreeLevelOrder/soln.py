# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Idea is to think of BFS, that explores a particular level before moving down.
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        queue = [root]
        while queue:
            row = []
            newQueue = []
            for node in queue:
                if node:
                    row.append(node.val)
                    newQueue.append(node.left)
                    newQueue.append(node.right)
            if row:
                result.append(row)
            queue = newQueue
        return result
        
