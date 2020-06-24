# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = head
        prev = ListNode(None)
        while start:
            if start.val == prev.val:
                start = start.next
                prev.next = start
            else:
                prev = start
                start = start.next
        return head
