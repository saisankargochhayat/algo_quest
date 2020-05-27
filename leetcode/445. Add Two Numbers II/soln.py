# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        result = None
        carry = 0
        while l1 is not None or l2 is not None:
            sum = 0
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            sum += carry
            sumNode = ListNode(sum%10)
            carry = sum//10
            sumNode.next = result
            result = sumNode
            # Equal length digits and carry is there 
            if l1 is None and l2 is None and carry != 0:
                lastNode = ListNode(carry)
                lastNode.next = result
                return lastNode
        return result
    
    
    # Takes a linked list and reverses it. 
    def reverse(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        curr, head.next, prev = head.next, None, head
        while curr:
            nextNode, curr.next = curr.next, prev
            prev, curr = curr, nextNode      
        return prev
