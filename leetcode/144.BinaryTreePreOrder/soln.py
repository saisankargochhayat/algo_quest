# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Preorder - root, left, right

#Iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                stack.append(curr.left)
        return res       
    
# Recursive
# class Solution:
#     res = []
    
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         self.res = []
#         self.printPreorder(root)
#         return self.res
        
#     def printPreorder(self, node):
#         if node:
#             self.res.append(node.val)
#             self.printPreorder(node.left)
#             self.printPreorder(node.right)
