class Solution:
    solution = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if (root == None):
            return 
        self.solution = []
        self.inorderHelper(root)
        return self.solution
    
    def inorderHelper(self, root: TreeNode):
        if (root == None):
            return 
        self.inorderHelper(root.left)
        self.solution.append(root.val)
        self.inorderHelper(root.right)
        
