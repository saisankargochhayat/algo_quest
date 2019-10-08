# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.path = []
        curr = root
        while curr:
            self.path.append(curr)
            curr = curr.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        minimum = self.path.pop()
        curr = minimum.right
        while curr:
            self.path.append(curr)
            curr = curr.left        
        return minimum.val

        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.path) > 0:
            return True
        else: 
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
