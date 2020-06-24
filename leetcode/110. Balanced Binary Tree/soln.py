# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:        
        def helper(root):
            nonlocal res
            if not root or not res:
                return 0
            leftHeight = helper(root.left)
            rightHeight = helper(root.right)
            if abs(leftHeight-rightHeight) > 1:
                res = False
            return max(leftHeight, rightHeight) + 1
        res = True
        height = helper(root)
        return res
