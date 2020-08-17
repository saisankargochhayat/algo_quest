# Lets duplicate the array to take care of the circular condition
# Now go through the elments and lets add to the stack
# And when we encounter a larger element pop the smaller ones and add to the dictionary if not encountered before. 
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res, stack = {}, []
        newnums = nums + nums
        for index, num in enumerate(newnums):
            while stack and stack[-1][1] < num:
                ind, elePopped = stack.pop()
                if ind not in res:
                    res[ind] = num
            stack.append((index, num))
        return [res[i] if i in res else -1 for i in range(len(nums))]


 def nextGreaterElements(self, A):
        stack, res = [], [-1] * len(A)
        for i in range(len(A)) * 2:
            while stack and (A[stack[-1]] < A[i]):
                res[stack.pop()] = A[i]
            stack.append(i)
        return res
