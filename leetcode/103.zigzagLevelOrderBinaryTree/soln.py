# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result, queue, direction = [], [root], True
        while queue:
            row = []
            nextQueue = []
            for node in queue:
                if node:
                    row.append(node.val)
                    if node.left: nextQueue.append(node.left)
                    if node.right: nextQueue.append(node.right)
            if len(row):
                if direction:
                    result.append(row)
                    direction = False
                else:
                    result.append(row[::-1])
                    direction = True
            queue = nextQueue
        return result
            
