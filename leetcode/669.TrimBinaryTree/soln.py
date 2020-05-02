# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trimTree(node):
            if not node:
                return None
            elif node.val < L:
                return trimTree(node.right)
            elif node.val > R:
                return trimTree(node.left)
            # Recursion on left and right, and return pruned results back
            # Nodes not to be pruned, recurse. 
            node.left = trimTree(node.left)
            node.right = trimTree(node.right)
            return node
            
        return trimTree(root)
