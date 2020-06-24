# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Rule out elements greater than R by not going Right than R. 
# Rule out elements smaller than L by not going more Left than L. 
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = 0
        def inOrder(root): 
            nonlocal res
            if root:
                if root.val >= L and root.val <= R:
                    res += root.val 
                if root.val >= L:
                    inOrder(root.left)
                if root.val <= R:
                    inOrder(root.right)
        inOrder(root)        
        return res
                	
