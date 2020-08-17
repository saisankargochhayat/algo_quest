class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiff = float('inf')
        res = None
        # The outer element takes the first element and compares rest all elements with it. 
        for i in range(len(nums)-2):
            start, end = i+1, len(nums)-1
            while start < end:
                tSum = (nums[i] + nums[start] + nums[end])
                diff = abs(target - tSum)
                # Exit early if zero found, i.e. closest 3Sum
                if diff == 0:
                        return tSum
                if diff < minDiff:
                    minDiff, res = diff, tSum
                # Because the array is sorted, we strive towards the target
                # Increasing the start, increases tSum amount and decreasing reduces tSum towards target. 
                if tSum < target:
                    start += 1
                else:
                    end -= 1
        return res
