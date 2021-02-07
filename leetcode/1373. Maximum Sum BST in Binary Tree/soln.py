# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        res = 0
        # Returns isBst, sum, minl, maxL
        def findMax(root):
            nonlocal res
            if not root:
                return None, 0, None, None # None node is a BST
            
            l_isBst, l_total, ll, lr = findMax(root.left) # Traverse left
            r_isBst, r_total, rl, rr = findMax(root.right) # Traverse right
            if ((l_isBst and (lr < root.val)) or l_isBst == None) and ((r_isBst and (rl > root.val)) or r_isBst == None):
                total = root.val + l_total + r_total
                res = max(total, res)
                return True, total, (ll if ll is not None else root.val), (rr if rr is not None else root.val) # Is a bst and we we return sum and min and max range. 
            return False, 0, None, None # Not a bst subtree
        
        findMax(root)
        return res
            