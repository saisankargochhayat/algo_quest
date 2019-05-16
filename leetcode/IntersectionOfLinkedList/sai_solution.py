# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        listA = headA
        countA = 0
        listB = headB
        countB = 0
        while listA is not None:
            listA = listA.next
            countA += 1
        while listB is not None:
            listB = listB.next
            countB += 1
        if countA > countB:
            offset = countA - countB
            while offset != 0:
                headA = headA.next
                offset -= 1
        else:
            offset = countB - countA
            while offset != 0:
                headB = headB.next
                offset -= 1
        intersection = 0
        offset = abs(countA - countB)
        while headA != None:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
                intersection += 1
        return None

        