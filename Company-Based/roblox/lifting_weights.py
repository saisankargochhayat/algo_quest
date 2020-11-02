def weightCapacity(weights, maxCapacity):
    values = weights.copy()
    n = len(weights)
    dp = [[0 for x in range(maxCapacity+1)] for y in range(len(weights)+1)]
    # Lets fill the dp table
    for i in range(len(weights)+1):
        for j in range(maxCapacity+1):
            # First row is basically zero
            if i == 0 or j == 0:
                dp[i][j] == 0
            elif weights[i-1] <= j:
                # if weight to be explored is less than max weight
                dp[i][j] = max(values[i-1]+ dp[i-1][j-weights[i-1]], dp[i-1][j])
            else:
                # We end up here if the current weight cant fit the maxCapacity
                dp[i][j] = dp[i-1][j]
    print(dp)
    return dp[n][maxCapacity]
            

weightCapacity([1,2,3,5], 7)