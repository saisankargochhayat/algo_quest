# Same idea as count subarrays with sum k #560
from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr = [1 if num % 2 else 0 for num in nums]
        cSum, ans = 0, 0
        mem = defaultdict(int)
        mem[0] = 1
        for i in range(len(nums)):
            cSum += arr[i]
            # print(cSum, cSum-k, mem, ans)
            if (cSum-k in mem):
                ans += mem[cSum-k]
            mem[cSum] += 1
        # print(arr)
        return ans
