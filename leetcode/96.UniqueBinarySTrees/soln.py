class Solution:
    def numTrees(self, n: int) -> int:
        cache = [None for _ in range(n+1)]
        res = self.countTrees(n, cache)
        return res
    
    def countTrees(self, n: int, cache: list) -> int:
        # Base cases
        if n == 0:
            return 1

        if cache[n]:
            return cache[n]
        
        result = 0
        for i in range(n):
            leftTrees = self.countTrees(i, cache)
            rightTrees = self.countTrees(n-i-1, cache)
            result += (leftTrees*rightTrees)
        cache[n] = result
        return result
