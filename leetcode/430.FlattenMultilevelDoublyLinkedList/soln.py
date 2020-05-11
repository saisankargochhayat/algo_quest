"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


# Stack approach
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # Empty head
        if head is None:
            return
        dummyNode = Node(None, None, head, None)
        prev = dummyNode
        
        stack = []
        stack.append(head)
        # We continue still stack exists.
        while stack:
            # Let's connect nodes after popping
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            # if next exist 
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        # detach dummy node
        res = dummyNode.next
        res.prev = None
        return res
        
        
# Now we take the source node and its start would point to child list, and child node to source node. 
# The child list's end node points to nextNode, and nextNode prev a last node. 
# One sneaky catch - if nextNode is empty point return head. 

# class Solution:
#     def flatten(self, head: 'Node') -> 'Node':
#         def flattenChildList(sourceNode, childNode, nextNode):
#             head = childNode
#             sourceNode.next = childNode
#             sourceNode.child = None
#             childNode.prev = sourceNode
#             while head != None:
#                 # End of the child list. 
#                 if head.next == None:
#                     head.next = nextNode
#                     if nextNode is None:
#                         return head
#                     nextNode.prev = head
#                     return nextNode
#                 elif head.child is None:
#                     head = head.next
#                 else:
#                     head = flattenChildList(head, head.child, head.next)
#             return nextNode
        
#         start = head
#         head = head
#         while head != None:
#             # we dont need to anything in this case. 
#             if head.child is None:
#                 head = head.next
#             else:
#                 # Flatten the list here. 
#                 head = flattenChildList(head, head.child, head.next)     
#         # self.checkAnswer(start)
#         return start
        
            

