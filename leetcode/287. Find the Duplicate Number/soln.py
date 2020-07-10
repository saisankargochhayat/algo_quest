# Think like linked list cycle 2. 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        # Finding intersection point inside cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Now we use the linked list cycle logic of 2(F+a) = F + a + x + a
        # F is is distance of start to start of cycle and a is cycle start to intersection point. 
        # We know from the equation F = x 
        slow = nums[0]
        while True:
            # Get the element that points to the cycle start no the intersection point. [3,1,3,4,2]
            if slow == fast:
                break
            slow = nums[slow]
            fast = nums[fast]
        return fast
        
