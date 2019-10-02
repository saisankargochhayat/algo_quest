#https://leetcode.com/problems/minimum-depth-of-binary-tree/solution/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Dfs solution
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        stack, minVal = [(root, 1),], float('inf')
        #stack, minVal = [(1, root),], float('inf')
        
        # Till stack has value
        while stack:
            node, currDepth = stack.pop()
            # if reached leaf node
            if node.left == None and node.right == None:
                minVal = min(minVal, currDepth)
            if node.left:
                stack.append((node.left, currDepth+1))
            if node.right:
                stack.append((node.right, currDepth+1))  
        return minVal  
                
        
        
        
    # def minDepth(self, root: TreeNode) -> int:
    #     if root == None:
    #         return 0
    #     children = [root.left, root.right]
    #     if root.left == None and root.right == None:
    #         return 1
    #     minVal = float('inf')
    #     for c in children:
    #         if c:
    #             minVal = min(self.minDepth(c),minVal)
    #     return minVal+1
