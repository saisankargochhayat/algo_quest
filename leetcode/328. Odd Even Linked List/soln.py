# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        curr = head
        oddDummy = ListNode(None)
        oddListHead = oddDummy
        while curr != None and curr.next != None:
            # Odd element element
            oddDummy.next = curr.next
            oddDummy = oddDummy.next
            # Jump to next even node.
            curr.next = curr.next.next
            curr = curr.next if curr.next != None else curr
            oddDummy.next = None
        curr.next = oddListHead.next
        return head
