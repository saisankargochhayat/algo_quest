import random
class Solution:
    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a binary search to find the target zone
        #print(self.prefix_sums, target)
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
        


# Linear Search
# import random
# class Solution:

#     def __init__(self, w: List[int]):
#         self.arr = w
#         self.s = sum(w)
#         self.idxArr = [0]
#         for i in w:
#             self.idxArr.append(self.idxArr[-1]+(i/self.s))
#         # print(self.idxArr)
 
#     def pickIndex(self) -> int:
#         num = random.random()
#         for i, p in enumerate(self.idxArr):
#             if num < p:
#                 return i-1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
