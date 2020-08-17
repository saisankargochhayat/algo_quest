# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We use the inorder to find which elements are left and right of the curr element. 
# And the post order to start with the first elemeent and then construct right and left trees.

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(inorderL, inorderR):
            # base case
            if inorderL >= inorderR:
                return None
            nonlocal postorder
            curr = postorder.pop()
            root = TreeNode(curr)
            currPos = inorderMap[curr]
            root.right = helper(currPos+1, inorderR)
            root.left = helper(inorderL, currPos)
            return root
        
        
        inorderMap = {v:k for k, v in enumerate(inorder)}
        return helper(0, len(inorder))