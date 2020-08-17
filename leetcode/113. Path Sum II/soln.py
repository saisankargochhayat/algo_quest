# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def helper(node, currPath, target):
            nonlocal res
            currPath.append(node.val)
            # Leaf node case
            if node.left is None and node.right is None and target == 0:
                res.append(currPath[:])
            
            # Call for left node 
            if node.left:
                helper(node.left, currPath[:], target - node.left.val)
            # and for right
            if node.right:
                helper(node.right, currPath, target - node.right.val)
            
            # We pop after the the child nodes have been solved, we dont have to copy the list in every stage of recursion. 
            currPath.pop()
        
        helper(node = root, currPath = [], target = sum-root.val)
        return res
    
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def helper(node, currPath, target):
            nonlocal res
            currPath.append(node.val)
            # Leaf node case
            if node.left is None and node.right is None and target == 0:
                res.append(currPath[:])
            
            # Call for left node 
            if node.left:
                helper(node.left, currPath[:], target - node.left.val)
            # and for right
            if node.right:
                helper(node.right, currPath[:], target - node.right.val)
            
        
        helper(node = root, currPath = [], target = sum-root.val)
        return res