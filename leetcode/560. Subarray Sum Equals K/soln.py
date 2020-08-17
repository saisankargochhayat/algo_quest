# sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.
 # Further, for every sum encountered, we also determine the number of times the sum sum-ksum−k has occured already, since it will determine the number of times a subarray with sum kk has occured upto the current index. We increment the countcount by the same amount.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        # For sum 0, it exists once already. 
        mem = defaultdict(int)
        # Necessary as currSum - k might be 0, in first occurance. 
        mem[0] = 1
        count = 0
        currSum = 0
        for i in nums:
            currSum += i
            if mem.get(currSum - k):
                # We fetch the element of last sum to keep track of combinations encountered already. 
                # Basically combinations of that sum possible + current numbers. 
                count += mem.get(currSum-k)
            mem[currSum] += 1
        return count
