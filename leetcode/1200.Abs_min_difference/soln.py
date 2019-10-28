class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum = min(b-a for a, b in zip(arr, arr[1:]))
        res = [[a,b] for a, b in zip(arr, arr[1:]) if b-a == minimum]
        return res
        
        
    
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
#         newArr = sorted(arr)
#         globalMin = float("inf")
#         for i in range(len(arr)-1):
#             curr = abs(newArr[i+1]-newArr[i])
#             globalMin = min(curr, globalMin)
#         res = []
#         for i in range(len(arr)-1):
#             if abs(newArr[i+1] - newArr[i]) == globalMin:
#                 res.append([newArr[i], newArr[i+1]])
#         return res
            

