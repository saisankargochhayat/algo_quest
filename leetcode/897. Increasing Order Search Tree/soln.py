# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# RT - O(N) and Space - O(H) h = height of tree
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inOrder(node):
            if node:
                inOrder(node.left)
                node.left = None
                self.curr.right = node
                self.curr = node
                inOrder(node.right)
        start = self.curr = TreeNode(None) 
        inOrder(root)
        return start.right
            

# class Solution:
#     def increasingBST(self, root: TreeNode) -> TreeNode:
#         start = TreeNode(None)
#         curr = start
#         def inOrder(root):
#             nonlocal curr
#             if not root:
#                 return
#             # left - root - right
#             inOrder(root.left)
#             curr.right = TreeNode(root.val)
#             curr = curr.right
#             inOrder(root.right)
#         inOrder(root)
#         return start.right
            