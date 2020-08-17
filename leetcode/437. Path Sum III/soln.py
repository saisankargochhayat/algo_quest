# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Backtracking approach
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        from collections import defaultdict
        count = 0
        def helper(node, currSum):
            nonlocal count
            currSum += node.val
            if mem.get(currSum - sum):
                count += mem.get(currSum - sum)
            mem[currSum] += 1
            if node.left:
                helper(node.left, currSum)
            if node.right:
                helper(node.right, currSum)
            # After both subtrees processed 
            mem[currSum] -= 1

        mem = defaultdict(int)
        mem[0] = 1
        if root:
            helper(root, 0)
        return count

# Copy of a hashmap is passed in the child nodes processed. 
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        from collections import defaultdict
        count = 0
        def helper(node, currSum, mem):
            nonlocal count
            currSum += node.val
            if mem.get(currSum - sum):
                count += mem.get(currSum - sum)
            mem[currSum] += 1
            if node.left:
                helper(node.left, currSum, mem.copy())
            if node.right:
                helper(node.right, currSum, mem.copy())

        mem = defaultdict(int)
        mem[0] = 1
        if root:
            helper(root, 0, mem)
        return count
    