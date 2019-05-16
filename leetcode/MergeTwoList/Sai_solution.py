# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = ListNode(0)
        ptr = newList
        while (l1 != None and l2 != None):
            if (l1.val <= l2.val):
                ptr.next = ListNode(l1.val)
                ptr = ptr.next
                l1 = l1.next
            else:
                ptr.next = ListNode(l2.val)
                ptr = ptr.next
                l2 = l2.next
        if (l1 == None):
            ptr.next = l2
        else:
            ptr.next = l1
        return newList.next
    
