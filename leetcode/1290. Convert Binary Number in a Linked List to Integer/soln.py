# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head: 
            ans = 2*ans + head.val 
            head = head.next 
        return ans 




# O(N) Space- O(N)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        res = 0
        def helper(curr):
            nonlocal res
            if curr == None:
                return 0
            c = helper(curr.next)
            res += 2**c * curr.val if curr.val else 0
            return c+1

        helper(curr)
        return res
    
    
