from typing import Collection, List
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        from heapq import heappush, heappop
        hp, res = [], []
        blacklist = set()
        start, end = 0, 0
        while len(hp) < k-1:
            heappush(hp, (-1*nums[end], end))
            end += 1
        # We have the reached k-1 elements in the heap
        while end < len(nums):
            heappush(hp, (-1*nums[end], end))
            val, index = heappop(hp)
            while index in blacklist and len(hp) > 0:
                val, index = heappop(hp)

            # We add the max element which is not blacklisted to the res and put it back in the heap
            res.append(-1*val)
            heappush(hp, (val, index))

            # this is where we slide the window. 
            blacklist.add(start)
            start += 1
            end += 1
        return res




print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))



# deque ensures that the elemetns less than bound are removed and the deque is always decreasing. 

def maxSlidingWindow1(nums: List[int], k: int) -> List[int]:
    from collections import deque
    q = deque()
    output = []
    for i in range(len(nums)):
        # if the queue's left element is out of bounds, pop it to maintain size
        if i-k >= 0 and nums[i-k] == q[0]:
                q.popleft()

        # ensure array is DECREASING by right-popping elements that are smaller
        while q and q[-1] < nums[i]: 
            q.pop()

        # add the element itself
        q.append(nums[i])

        # append to output list if we have full window
        if i >= k-1:
            output.append(q[0])

    return output