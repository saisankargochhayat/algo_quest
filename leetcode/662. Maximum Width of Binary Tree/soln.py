# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        from collections import deque
        if not root:
            return 0
        max_width = 0
        queue = deque()
        queue.append((root, 0))
        while queue:
            level_length = len(queue)
            _, level_head_index = queue[0]
            nextLevel = deque()

            for curr in queue:                
                node, col_index = curr
                # Preparing next level
                if node.left:
                    nextLevel.append((node.left, 2 * col_index))
                if node.right:
                    nextLevel.append((node.right, 2 * col_index + 1))
            # calculate the length of the current level,
            #   by comparing the first and last col_index.
            max_width = max(max_width, col_index - level_head_index + 1)
            #print([node if node != None else None for node in nextLevel])
            queue = nextLevel
            
        return max_width


# Official BFS Solution.
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        from collections import deque
        if not root:
            return 0

        max_width = 0
        # queue of elements [(node, col_index)]
        queue = deque()
        queue.append((root, 0))

        while queue:
            level_length = len(queue)
            _, level_head_index = queue[0]
            # iterate through the current level
            for _ in range(level_length):
                node, col_index = queue.popleft()
                # preparing for the next level
                if node.left:
                    queue.append((node.left, 2 * col_index))
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))

            # calculate the length of the current level,
            #   by comparing the first and last col_index.
            max_width = max(max_width, col_index - level_head_index + 1)

        return max_width


        
# Slow BFS (Times out)
# class Solution:
#     def widthOfBinaryTree(self, root: TreeNode) -> int:
#         currLevel = [root]
#         mWidth = 1 if root else 0
#         while len(currLevel):
#             nextLevel = []
#             for node in currLevel:
#                 if node:
#                     nextLevel.append(node.left)
#                     nextLevel.append(node.right)
#                 else:
#                     # If there is a null node the children are also two nulls.
#                     nextLevel.extend([None,None])
#             currLevel = nextLevel
#             mWidth = max(mWidth, self.calcWidth(nextLevel))
#             if not any(nextLevel):
#                 currLevel = []
#         return mWidth
    
#     def calcWidth(self, currLevel):
#         # print([node.val if node != None else None for node in currLevel])
#         start, end = None, None
#         for i in range(len(currLevel)):
#             if start == None and currLevel[i] != None:
#                 start = i
#                 end = i
#             elif currLevel[i] != None:
#                 end = i
#         # print(end, start)
#         return (end - start) + 1 if start != None else 0
        
            