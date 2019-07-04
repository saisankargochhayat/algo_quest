# Problem - https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = [0 for i in range(amount+1)]
        count[0] = 0
        last_coin = [0 for i in range(amount+1)]
        for i in range (1, amount+1):
            minimum = float("inf")
            for j in range(len(coins)):
                #print(coins[j], i)
                if coins[j] <= i:
                    if ((1+count[i-coins[j]]) < minimum):
                        minimum = 1 + count[i-coins[j]]
                        coin = coins[j]
            count[i] = minimum
            #print(count[i])
            #last_coin[i] = coin
        if (count[amount]) == float("inf"):
            return -1
        return count[amount]