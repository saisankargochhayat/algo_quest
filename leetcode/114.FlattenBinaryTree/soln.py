# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# The idea is reverse pre-order traversal, where as we keep backtracking, we change pointers to old node. So the order is right - left - center

class Solution:
    prev = None
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.preTraverse(root)
        
        
    def preTraverse(self, node):
        # If empty node is passed.
        if not node:
            return None
        self.preTraverse(node.right)
        self.preTraverse(node.left)
        
        
        node.right = self.prev
        node.left = None
        self.prev = node
