# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Incase there is only one element.
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            # Preserve the first node here.
            a = pre.next
            # next node here
            b = a.next
            # Point first node to second node's next
            a.next = b.next
            # current counter to second node.
            pre.next = b
            #current counters next to prev node.
            pre.next.next = a
            # increase counter for traversal
            pre = pre.next.next
        return dummy.next
