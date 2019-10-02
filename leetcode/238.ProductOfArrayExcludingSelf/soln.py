class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardArray = []
        c = 1
        length = len(nums)
        output = [0]*length
        # Because there is nothing left of L[0]
        output[0] = 1
        for i in range(1,len(nums)):
            output[i] = output[i-1]*nums[i-1]
        # Starting from right and fidning products.
        c = 1   
        for j in range(length-2, -1, -1):
            c = c*nums[j+1]
            output[j] = output[j]*c            
        return output
                


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         forwardArray = []
#         c = 1
#         lenOfNums = len(nums)
#         for i in nums:
#             c = c*i
#             forwardArray.append(c)
#         reverseArray = []
#         c = 1
#         for j in reversed(range(lenOfNums)):
#             c = c*nums[j]
#             reverseArray.append(c)
#         reverseArray.reverse()
#         output = []
#         for i in range(lenOfNums):
#             if i == 0:
#                 output.append(reverseArray[i+1])
#             elif i == lenOfNums-1:
#                 output.append(forwardArray[i-1])
#             else:
#                 output.append(forwardArray[i-1]*reverseArray[i+1])
#         return output


