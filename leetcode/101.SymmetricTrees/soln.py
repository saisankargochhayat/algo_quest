# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkList(self, listA, listB):
        if len(listA) != len(listB):
            return False
        else:
            l = len(listA)
            for i in range(l):
                # print("here", listA[i], listB[l-i-1])
                if (listA[i] == None and listB[l-i-1] != None) or (listA[i] != None and listB[l-i-1] == None):
                    return False
                elif (listA[i] == None and listB[l-i-1] == None):
                    continue
                if listA[i].val != listB[l-i-1].val:
                    return False                
            return True 
        
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        elif root.left == None and root.right == None:
            return True
        elif root.left == None or root.right == None:
            return False
        if root.left.val == root.right.val:
            lQueue, rQueue = [], []
            lQueue.append(root.left)
            rQueue.append(root.right)
            while lQueue and rQueue:
                tempL, tempR = [], []
                # the mirror check.
                #print(lQueue, rQueue[::-1])
                if not self.checkList(lQueue, rQueue):
                    return False
                #BFS for left tree
                for ele in lQueue:
                    if ele != None:
                        tempL.append(ele.left)
                        tempL.append(ele.right)
                for ele in rQueue:
                    if ele != None:
                        tempR.append(ele.left)
                        tempR.append(ele.right)
                lQueue = tempL
                rQueue = tempR
            if lQueue == rQueue:
                return True 
        return False    
        
