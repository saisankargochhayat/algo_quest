class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # because you can start from cost[0] or cost[1]
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])
            
    # Naive dp
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         l = len(cost)
#         cost.append(0)
#         dp = [float("inf")]*(l+1)
#         return self.minPath(cost, dp, l)
    
#     def minPath(self, cost, dp, n):
#         if n == 0:
#             return cost[0]
#         elif n == 1:
#             return cost[1]            
#         else:
#             dp[n] = min(self.minPath(cost, dp, n-1)+cost[n], self.minPath(cost, dp, n-2)+cost[n])
#             return dp[n]
            
        
