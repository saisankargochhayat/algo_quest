n,m = list(map(int,input().split(' ')))
coins = list(map(int,input().split(' ')))
dp =[ [-1 for x in range(m+1)] for y in range(n+1) ]
def getCount(amount,index):
    if amount == 0:
        return 1
    if index == 1:
        coin = coins[0]
        if amount%coin == 0:
            return 1
        else:
            return 0
    if dp[amount][index] != -1:
        return dp[amount][index]
    ans = 0
    parts = int(amount/(coins[index-1]))
    for i in range(parts+1):
        got = int(getCount(amount - i*coins[index-1],index-1))
        ans = ans+got
    dp[amount][index] = ans
    return ans
print(getCount(n,m))
