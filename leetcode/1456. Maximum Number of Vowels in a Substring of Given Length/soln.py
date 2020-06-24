class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left, right = 0, 0 
        ans, l, count = 0, len(s), 0
        vowels = {'a','e','i','o','u'}
        while right < l:
            if s[right] in vowels:
                count += 1
            # Shrink window if size > k 
            if (right - left + 1) > k:
                if s[left] in vowels:
                    count -= 1
                left += 1
            right += 1
            ans = max(count, ans)
        return ans
