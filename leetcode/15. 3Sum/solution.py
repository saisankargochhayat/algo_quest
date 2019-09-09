class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        for i in range(len(nums)-2):
            # sum of the numbers greater than this would always be positive.
            if nums[i] > 0: break
            # Avoid same i again.
            if i > 0 and nums[i] == nums[i-1]: continue
            start = i+1
            end = len(nums)-1
            while (start < end):
                sumTriplet = nums[i] + nums[start] + nums[end]
                if (sumTriplet) == 0:
                    solution.append([nums[i], nums[start], nums[end]])
                    # keep sliding to prevent same numbers.
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    # keep sliding backwards to prevent same numbers.
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif sumTriplet < 0:
                    start += 1
                elif sumTriplet > 0:
                    end -= 1
        return solution