class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        length = len(S)
        res = [length]*length
        prev = -float('inf')
        for i in range(length):
            if (S[i] == C): prev = i
            res[i] = min(res[i], abs(i-prev))
        for i in range(length)[::-1]:
            if (S[i] == C): prev = i
            res[i] = min(res[i], abs(i-prev))
        return res
        
        
        
# # Brute force
# class Solution:
#     def shortestToChar(self, S: str, C: str) -> List[int]:
#         soln = [-1]*len(S)
#         eIndex = []
#         for i in range(len(S)):
#             if S[i] == C:
#                 soln[i] = 0
#                 eIndex.append(i)
#         for j in range(len(S)):
#             minDis = float("inf")
#             for k in eIndex:
#                 minDis = min(abs(k-j), minDis)
#             soln[j] = minDis
#         return soln
