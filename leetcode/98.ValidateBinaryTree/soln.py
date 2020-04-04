# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        if root:
            treeData = []
            self.inOrder(root, treeData)
            l = [node.val for node in treeData]
            # Check if inorder is sorted
            if all(l[i] > l[i+1] for i in range(len(l)-1)):
                return True
            else:
                return False
        return True
            
    
    def inOrder(self, root: TreeNode, treeData) -> bool:
        if root:
            self.inOrder(root.right, treeData)
            treeData.append(root)
            self.inOrder(root.left, treeData)
