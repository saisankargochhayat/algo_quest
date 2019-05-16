# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def find_max_subarray(self, A, low, high):
        # means only one element present.
        if high == low:
            return (low, high, A[low])
        else:
            mid = (low + high) // 2
            left_low, left_high, left_sum = self.find_max_subarray(A, low, mid)
            right_low, right_high, right_sum = self.find_max_subarray(A, mid+1, high)
            cross_low, cross_high, cross_sum = self.find_max_crossing_subarray(A, low, mid, high)
            if left_sum >= right_sum and left_sum >= cross_sum:
                return (left_low, left_high, left_sum)
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return (right_low, right_high, right_sum)
            else:
                return (cross_low, cross_high, cross_sum)
    
    def find_max_crossing_subarray(self, A, low, mid, high):
        left_sum = -(math.inf)
        sum = 0
        max_left, max_right = 0, 0
        for i in range(mid, low-1, -1):
            sum = sum + A[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i
        right_sum = -(math.inf)
        sum = 0
        for j in range(mid+1, high+1):
            sum = sum + A[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j
        return (max_left, max_right, left_sum+right_sum)
        
    def maxSubArray(self, nums: List[int]) -> int:
        # bestSum = min(nums)
        # tailSum = 0
        
        # for n in nums:
        #     tailSum += n
        #     bestSum = max(tailSum, bestSum)
        #     tailSum = max(tailSum, 0)
                
        # return bestSum

        # divide and conquer soln below
        max_left, max_right, max_sum = self.find_max_subarray(nums, 0, len(nums)-1)
        #print(max_left, max_right)
        return max_sum
    

        