# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = None
        self.c = 0
        self.traverse(root, k, self.c, self.res)
        return self.res
    def traverse(self, root: TreeNode, k: int, c: int, res: int):
        if root == None or self.res != None:
            return
        self.traverse(root.left, k, self.c, self.res)
        self.c += 1
        if self.c == k and self.res == None:
            self.res = root.val
            return
        self.traverse(root.right, k, self.c, self.res)
