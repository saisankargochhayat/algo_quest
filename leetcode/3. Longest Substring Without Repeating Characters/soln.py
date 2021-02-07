class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        c_chars = defaultdict(int)
        l, r, res = 0, 0, 0
        contract = False
        while r < len(s):
            # Expand 
            if s[r] in c_chars and c_chars[s[r]] > 0: # check if contract is needed
                contract = True
            c_chars[s[r]] += 1
            r += 1
            
            # Contract 
            if contract:
                d_char = s[r-1] # Char to remove
                while s[l] != d_char and l < r:
                    c_chars[s[l]] -= 1 
                    l += 1
                c_chars[s[l]] -= 1
                l += 1
                contract = False

            res = max(res, r-l)
        return res