"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        start = head
        head = head
        while head != None:
            # we dont need to anything in this case. 
            if head.child is None:
                head = head.next
            else:
                # Flatten the list here. 
                head = self.flattenChildList(head, head.child, head.next)     
        # self.checkAnswer(start)
        return start
    
    # def checkAnswer(self, head):
    #     while head:
    #         print(head.val, head.prev)
    #         head = head.next
        
            
    # Now we take the source node and its start would point to child list, and child node to source node. 
    # The child list's end node points to nextNode, and nextNode prev a last node. 
    # One sneaky catch - if nextNode is empty point return head. 
    def flattenChildList(self, sourceNode, childNode, nextNode):
        head = childNode
        sourceNode.next = childNode
        sourceNode.child = None
        childNode.prev = sourceNode
        while head != None:
            # End of the child list. 
            if head.next == None:
                head.next = nextNode
                if nextNode is None:
                    return head
                nextNode.prev = head
                return nextNode
            elif head.child is None:
                head = head.next
            else:
                head = self.flattenChildList(head, head.child, head.next)
        return nextNode
