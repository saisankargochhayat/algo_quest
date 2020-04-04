# So the numbers we have seen before lead to endless recursion.
class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in cache:
                return False
            cache.add(n)
        return True
    
