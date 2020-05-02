# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverseList(head: ListNode) -> ListNode:
            if head == None:
                return
            prev = head
            curr = head.next
            head.next = None
            while curr != None:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev
        if head == None:
            return True
        
        l = 0
        start = head
        # First we find length of list
        while start != None:
            l += 1
            start = start.next

        # Now we try two pointer approach
        secondStart, secondHead = l//2, head
        count = 0
        while count < secondStart:
            count += 1
            secondHead = secondHead.next
        # if l is odd, we skip the center
        secondHead = secondHead.next if l % 2 != 0 else secondHead       
     
        # Finally check for palindrome
        first, second = head, reverseList(secondHead)
        while second != None:
            if first.val == second.val:
                first = first.next
                second = second.next
            else:
                return False        
        return True
        
