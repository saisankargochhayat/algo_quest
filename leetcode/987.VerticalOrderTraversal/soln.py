# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Idea is to traverse and get coordinates and the value.
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # Lets get all the nodes as a list of x,y, and value in a list. 
        arr = []
        self.getTraversalList(root, 0, 0, arr)
        resDict = defaultdict(list)
        for tup in arr:
            resDict[tup[0]].append(tup)
        keys = sorted(resDict.keys())
        # Swap if same coordinate
        self.swapVal(resDict, keys)
        # Finally create the output
        output = []
        for i in keys:
            output.append(resDict[i])
        return output
        
    # We collect all nodes as [x,y,node val]
    def getTraversalList(self, node, x, y, arr):
        if node:
            arr.append([x,y,node.val])
            self.getTraversalList(node.left, x-1, y-1, arr)
            self.getTraversalList(node.right, x+1, y-1, arr)
    
    #Vertical sorting and same value value sorting.
    def swapVal(self, resDict, keys):
        for key in keys:
            val = resDict[key]
            tempDict = defaultdict(list)
            for node in val:
                tempDict[(node[0], node[1])].append(node)
            #Vertical sorting
            sortedTempKeys = sorted(tempDict.keys(), key= lambda x:x[1], reverse=True)
            finalVal = []
            for i in sortedTempKeys:
                tempVal = tempDict[i]
                # Same coordinate value sorting.
                tempVal = sorted(tempVal, key= lambda x:x[2])
                for _,_,v in tempVal:
                    finalVal.append(v)
            resDict[key] = finalVal
                
                

# Sorted takes care of sort by first, then second value.             
from collections import defaultdict
class Solution(object):
    def helper(self, placement,level, root, dic):
        if(not root):
            return
        dic[placement].append((level, root.val))
        self.helper(placement-1, level+1, root.left, dic)
        self.helper(placement+1, level+1, root.right, dic)
		
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(list)
        self.helper(0,0, root, dic)
        result = []
        for i in sorted(dic.keys()):
            temp = []
            for j in sorted(dic[i]):
                temp.append(j[1])
            result.append(temp)
        return result
