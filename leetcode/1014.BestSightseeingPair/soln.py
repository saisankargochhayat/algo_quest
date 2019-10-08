class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxAi, result = 0, 0
        # max Ai keeps track of best encountered till now A[i]+i.
        # result keeps finding better results across all j's.
        for j in range(len(A)):
            result = max(maxAi+A[j]-j, result)
            maxAi = max(maxAi, A[j]+j)
        return result
    

# Slightly better solution.
#     def maxScoreSightseeingPair(self, A: List[int]) -> int:
#         maxScore = -float('inf')
#         ele1 = 0
#         ele2 = ele1+1
#         l = len(A)
#         for ele2 in range(1, l):
#             currScore = self.findScore(A, ele1, ele2)
#             maxScore = max(maxScore, currScore)
#             newEle1 = ele1+1
#             tempScore = currScore
#             while newEle1 < ele2:       
#                 newScore = self.findScore(A, newEle1, ele2)
#                 if newScore > tempScore:
#                     tempScore = newScore
#                     maxScore = max(tempScore, maxScore)
#                     ele1 = newEle1
#                 newEle1 += 1 
#         return maxScore
    
#     Brute Force solution O(n^2)
#     def maxScoreSightseeingPair(self, A: List[int]) -> int:
#         maxScore = -float('inf')
#         for i in range(len(A)-1):
#             for j in range(i+1, len(A)):
#                 maxScore = max(maxScore, self.findScore(A, i, j))
#         return maxScore
    
#     def findScore(self, A, i, j):
#         return A[i] + A[j] + i - j
