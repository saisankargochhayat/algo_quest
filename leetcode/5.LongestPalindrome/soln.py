class Solution:
    def longestPalindrome(self, s):
        soln = ""
        for i in range(len(s)):
            # check for odd cases
            res = self.helper(s, i, i)
            if len(res) > len(soln):
                soln = res
            # check for even solution
            res = self.helper(s, i, i+1)
            if len(res) > len(soln):
                soln = res
        return soln           
            
    def helper(self, s, l, r):
        # This is a way to expand the string starting from i and break out when palindromic condition breaks. 
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l+1:r]
