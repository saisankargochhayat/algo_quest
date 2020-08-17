# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Stack approach
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, sum - root.val)]
        while stack:
            node, currPathSum = stack.pop()
            # if leaf node and path sum is exactly required 
            if not node.left and not node.right and currPathSum == 0:
                return True
            if node.left:
                stack.append((node.left, currPathSum - node.left.val))
            if node.right:
                stack.append((node.right, currPathSum - node.right.val))


# Top down recursion approach
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def helper(root, curr, s):
            if not root:
                return
            # If leaf node we check if sum is achieved we return true. 
            if root.left == None and root.right == None:
                if curr + root.val == s:
                    return True
            left = helper(root.left, curr + root.val, s)
            right = helper(root.right, curr + root.val, s)
            return left or right
        
        return helper(root, 0, sum)


    
