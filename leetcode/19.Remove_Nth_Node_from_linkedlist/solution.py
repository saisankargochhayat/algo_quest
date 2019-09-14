# two pass
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lenOfList = 0
        curr = head
        while curr != None:
            lenOfList += 1
            curr = curr.next
        counter = 0
        start = ListNode(0)
        start.next = head
        curr = start
        while counter < (lenOfList-n):
            curr = curr.next
            counter += 1
        tempNext = curr.next
        if (tempNext != None):
            tempNext = tempNext.next            
        curr.next = tempNext       
        return start.next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyNode = ListNode(0)
        dummyNode.next = head
        
        fast = dummyNode
        slow = dummyNode
        counter = 0
        while fast.next != None:
            fast = fast.next
            counter += 1
            if counter > n:
                slow = slow.next
        slow.next = slow.next.next
        return dummyNode.next