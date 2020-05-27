## Two way mountain walk
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i, j, n = 0, len(A)-1, len(A)
        # Person 1 climb towards the hill
        while i+1 < n and A[i] < A[i+1]:
            i += 1
        while j-1 > 0 and A[j-1] > A[j]:
            j -= 1
        return 0 < i == j < n - 1
        
        
# One way mountain walk
# class Solution:
#     def validMountainArray(self, A: List[int]) -> bool:
#         increasing = True
#         l = len(A)
#         # Catch small and only decreasing series. 
#         if len(A) < 3 or A[0] >= A[1]:
#             return False
#         for i in range(l-1):
#             # Decreasing starts here and it was still increasing till here. 
#             # Can be set only once. 
#             if A[i+1] <= A[i] and increasing:
#                 increasing = False
#             if not increasing and A[i+1] >= A[i]:
#                 return False
#         # Catch only increasing array
#         return True if not increasing else False
                
                
