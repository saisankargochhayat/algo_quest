class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for index, num in enumerate(nums2):
            while stack and stack[-1] < num:
                elePopped = stack.pop()
                res[elePopped] = num
            stack.append(num)
        ans = [res[num] if num in res else -1 for num in nums1]
        return ans
