# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s:
            queue = [s]
            while queue:
                nextWave = []
                for node in queue:
                    if t.val == node.val and self.compareHelper(t, node):
                        return True
                    if node.left:
                        nextWave.append(node.left)
                    if node.right:
                        nextWave.append(node.right)
                queue = nextWave                   
        return False

    def compareHelper(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None and t == None:
            return True
        elif s == None or t == None:
            return False  # Catch one of them is none
        elif s.val == t.val:
            return all([self.compareHelper(s.left, t.left),self.compareHelper(s.right,t.right)])
        else:
            return False