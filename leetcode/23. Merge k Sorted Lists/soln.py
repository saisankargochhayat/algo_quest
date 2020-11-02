class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return  # Handle empty k lists case
        
        from heapq import heappush, heappop
        resList = ListNode(None)
        hp = []
        # Lets fill the heap till k elements
        for lList in lists:
            if lList:   # Filter out None linked lists
                heappush(hp, (lList.val, id(lList), lList))
        
        curr = resList
        while hp:
            value, _, lList = heappop(hp)
            curr.next = ListNode(value)
            # if there are more nodes in the linkedlist lets put it back in the heap
            if lList.next:
                nextNode = lList.next
                heappush(hp, (nextNode.val, id(nextNode), nextNode))
            curr = curr.next # Advance the pointer to next node. 
        return resList.next



# Override listnode. 

# def __lt__(self,other):
#     return self.val<other.val
# ListNode.__lt__ = __lt__
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         h = []
#         for n in lists:
#             if n:
#                 heapq.heappush(h,n)
#         dummy = head = ListNode(0)
#         while h:
#             cur = heapq.heappop(h)
#             head.next = cur
#             head = head.next
#             if cur and cur.next:
#                 heapq.heappush(h,cur.next)
#         return dummy.next