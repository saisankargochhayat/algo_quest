class Solution:
    @staticmethod
    def getLetter(p: int):
        """Return character for a number like 1 returns 'a'."""
        return chr(96+p)
    
    def getSmallestString(self, n: int, k: int) -> str:
        res = []
        while n > 0:
            # print(n-1 * 26)
            if ((n-1) * 26) > k-1:
                res.append('a')  # Put a's in a greedy manner
                n -= 1
                k -= 1
            else:
                # Append the letter 
                temp = k - ((n-1)*26)
                if temp > 0:
                    res.append(self.getLetter(temp))
                    k -= temp
                    n -= 1
                remaining = 'z'*(k//26)
                res.append(remaining)
                n = 0
        return "".join(res)
