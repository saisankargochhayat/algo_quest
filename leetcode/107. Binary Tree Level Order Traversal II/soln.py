# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Using Recursion
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # Starting a new level
            if len(levels) == level:
                levels.append([])
            # Append the node to its appropriate level
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
                
        
        helper(root, 0)
        return levels[::-1]

# BFS
# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         res = []
#         temp = [root]
#         while temp:
#             row, nextTemp = [], []
#             for node in temp:
#                 if node:
#                     row.append(node.val)
#                     nextTemp.append(node.left)
#                     nextTemp.append(node.right)
#             if row:
#                 res.append(row)
#             temp = nextTemp
#         return res[::-1]
