# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Naive solution - create a hashmap, store node.val as key and value as index 
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         mem = set()
#         mem.add(head)
#         while head != None:
#             head = head.next
#             if head in mem:
#                 return head
#             mem.add(head)
#         return None


# Fast pointer slow pointer approach
# 2*(F+a) = F + a + b + a
class Solution(object):
    def getIntersect(self, head):
        slowPointer, fastPointer = head, head
        # We only check fast-pointer as its more likely to reach end in an acyclic chain. 
        while fastPointer is not None and fastPointer.next is not None:
            # We increase slowPointer to next node. 
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next            
            if fastPointer == slowPointer:
                return slowPointer
        return None

    def detectCycle(self, head):
        if head is None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an entrance to
        # a cycle.
        intersect = self.getIntersect(head)
        if intersect is None:
            return None
        
        # If its not acyclic let's find start of cycle point. 
        # We use the fact that the length from the intersection 
        # point is same as head node to intersection. 
        start = head
        while start is not intersect:
            start = start.next
            intersect = intersect.next
        return intersect

