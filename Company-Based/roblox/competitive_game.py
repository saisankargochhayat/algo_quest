def numPlayers(n, k, scores):
    buckets = [0] * 101
    # We filled the buckets
    for score in scores:
        buckets[score] += 1
    countRank,j = 0, 100
    res = 0
    # We start counting rank from 100. 
    print(buckets)
    while j > 0 and k > 0:
        countRank += 1
        res += buckets[j]
        k -= buckets[j]
        j -= 1
    return res

print(numPlayers(4,4,[100, 50, 50, 50, 50, 50, 25]))
