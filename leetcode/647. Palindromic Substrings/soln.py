class Solution:
    def countSubstrings(self, s: str) -> int:
        # So we know palindromes can be centered around, s[i] or around s[i],s[i+1]
        length, ans = len(s), 0
        # Cound odd palindromes
        for i in range(length):
            l, r = s[i], s[i]
            while l >= 0 and r <= length and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        # Count even palindromes
        for j in range(length-1):
            l, r = s[j], s[j+1]
            while l >= 0 and r <= length and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans  


# Trick of expanding range. 

class Solution:
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for center in range(2*N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans


# Naive solution generate all substrings and check if palindrome or not. 

class Solution:
    def countSubstrings(self, s: str) -> int:
        l, res = len(s), 0
        # The outer loop controls the length of the substring. 
        for start in range(l+1):
            # This is the end of the substring.
            for end in range(start+1, l+1):
                # End index
                temp = s[start:end]
                if temp == temp[::-1]:
                    res += 1
        return res