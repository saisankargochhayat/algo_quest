# 1) Create an empty stack S.
# 2) Initialize current node as root
# 3) Push the current node to S and set current = current->left until current is NULL
# 4) If current is NULL and stack is not empty then 
#      a) Pop the top item from stack.
#      b) Print the popped item, set current = popped_item->right 
#      c) Go to step 3.
# 5) If current is NULL and stack is empty then we are done.
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        current = root
        solution = []
        stack = []
        # Go down till the left most node.
        while True:
            while current != None:
                stack.append(current)
                current = current.left
            # Exit out of the infinite loop.
            while len(stack) == 0 and current == None:
                return solution
            while current == None and len(stack) > 0:
                popped_item = stack.pop()
                solution.append(popped_item.val)
                current = popped_item.right