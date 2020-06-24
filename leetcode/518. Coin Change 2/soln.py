# DP way of thought - 

# Bottom-up bulding solution.
# Base case amount or num of coins is zero, then num of combination = 1
# Now the strategy is here:

#     Add coins one-by-one, starting from base case "no coins".

#     For each added coin, compute recursively the number of combinations for each amount of money from 0 to amount.

# Algorithm

#     Initiate number of combinations array with the base case "no coins": dp[0] = 1, and all the rest = 0.

#     Loop over all coins:

#         For each coin, loop over all amounts from 0 to amount:
#             For each amount x, compute the number of combinations: dp[x] += dp[x - coin].

#     Return dp[amount].
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1

        # This is a 1-d DP solution space where we iterate over all the coins we have like starting from 2 in [2,5,10]
        for coin in coins:
            # Because adding a high value coin wont impact combinations of values lower than the coin's value. 
            for j in range(coin, amount+1):
                dp[j] = dp[j] + dp[j-coin]
        
        return dp[-1]
    
# Top-down approach 
# We start with coin 10 in [2,5,10] first and amount
# And also check for other options in the coin, and build the solution space. 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Extra row for when no coins 
        dp = [[None for i in range(amount+1)] for j in range(len(coins)+1)]
        # coinsUsed - numbers of different coins allowed to use for building amount
        def coinChange(coins, coinsUsed, amount, dp):
            if amount == 0:
                return 1
            # No way to make this amount. 
            if amount < 0 or coinsUsed == 0:
                return 0
            # Memory
            if dp[coinsUsed][amount] != None:
                return dp[coinsUsed][amount]
            res = 0
            # If is it possible using this coin 
            coin = coins[coinsUsed-1]
            res += coinChange(coins, coinsUsed, amount-coin, dp)
            
            # If possible using another coin
            res += coinChange(coins, coinsUsed-1, amount, dp)
            dp[coinsUsed][amount] = res
            return res
        
        ans = coinChange(coins, len(coins), amount, dp)
        print(dp)
        return ans
