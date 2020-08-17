# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# We would need to create an map out of in-order array to access index easily

class Solution:
    # Faster solution
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left=0, in_right=len(inorder)):
            # Using index in preorder list.
            nonlocal pre_idx
            # base cases
            if in_right <= in_left:
                return None
            
            # Preorder element left set as the curr node. 
            node_val = preorder[pre_idx]
            node = TreeNode(node_val)
            # We find where this element in 
            in_idx = inorderMap[node_val]
            # Finally increase to the next index in preorder
            pre_idx += 1            
            
            # left
            node.left = helper(in_left, in_idx)
            # right
            node.right = helper(in_idx  + 1, in_right)
            # Finally return the node as root for that level
            return node
        
        # Index element to set to zeroth element of preorder. 
        pre_idx = 0
        # Hashmap of value to index of inOrder array.
        inorderMap = {v:k for k,v in enumerate(inorder)}
        return helper()
    
    
    # def buildTree(self, preorder, inorder):
    #     if inorder:
    #         ind = inorder.index(preorder.pop(0))
    #         root = TreeNode(inorder[ind])
    #         root.left = self.buildTree(preorder, inorder[0:ind])
    #         root.right = self.buildTree(preorder, inorder[ind+1:])
    #         return root
