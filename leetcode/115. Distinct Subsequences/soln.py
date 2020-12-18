from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(maxsize=None)
        def helper(i, j):
            M, N = len(s), len(t)
            
            if i == M or j == N or M-i < N-j:
                return int(j == N)

            # if i of s and j of s dont match or match either case we skip
            ans = helper(i+1, j)
            # if it matches we skip both
            if s[i] == t[j]:
                ans += helper(i+1, j+1) 
            return ans
        res = helper(0,0)
        return res



class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # Dictionary for memoization
        mem = {}
        
        def helper(i, j):
            
            M, N = len(s), len(t)
            
            # Base case
            if i == M or j == N or M - i < N - j:
                return int(j == len(t))
            
            # Check if the result is already cached
            if (i, j) in mem:
                return mem[i,j]
            
            # Always make this recursive call
            ans = helper(i + 1, j)
            
            # If the characters match, make the other
            # one and add the result to "ans"
            if s[i] == t[j]:
                ans += helper(i + 1, j + 1)
            
            # Cache the answer and return
            mem[i, j] = ans
            return ans                
        
        return helper(0, 0)