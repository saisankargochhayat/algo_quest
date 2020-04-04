# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        if root == None:
            return []
        while len(stack) > 0:
            res.append(stack[-1:][0].val)
            newStack = []
            for i in stack:
                if i.left is not None:
                    newStack.append(i.left)
                if i.right is not None:
                    newStack.append(i.right)
            stack = newStack
        return res
    
    # DFS + stack
    def rightSideView(self, root):
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if curr:
                if len(res) == level:
                    res.append(curr.val)
                stack.append((curr.left, level+1))
                stack.append((curr.right, level+1))
        return res
