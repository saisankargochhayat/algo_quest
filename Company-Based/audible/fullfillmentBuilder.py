# Algo to find minimum N parts together. 
# Time taken to two parts together == sum of sizes
# Only two parts can be put together at a time. 

def combineParts(parts):
    from heapq import heappop, heappush
    hp, res = [], 0 
    for part in parts:
        heappush(hp, part)
    while len(hp) > 1:
        first = heappop(hp)
        second = heappop(hp)
        res += (first+second)
        heappush(hp, first+second)
    return res



print(combineParts([8,4,6,12]))