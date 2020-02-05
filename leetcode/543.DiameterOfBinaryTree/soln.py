# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    result = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(node: TreeNode) -> int:
            if node is None:
                return 0
            # depth of left node and right node
            left = depth(node.left)
            right = depth(node.right)
            self.result = max(self.result, left+right)
            return max(left, right)+1
        depth(root)
        return self.result
            
        
