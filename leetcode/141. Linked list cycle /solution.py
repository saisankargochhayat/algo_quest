# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slowRacer = head.next
        if slowRacer != None:
            fastRacer = head.next.next
        else: 
            return False
        while (slowRacer != fastRacer):
            if (fastRacer == None or fastRacer.next == None):
                return False
            slowRacer = slowRacer.next
            fastRacer = fastRacer.next.next
        return True
        