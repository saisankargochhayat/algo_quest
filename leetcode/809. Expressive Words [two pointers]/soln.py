from typing import List
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def compressWord(word: str) -> List:
            newStr = []
            i, l = 0, len(word)
            while i < len(word):
                counter, char = 1, word[i]
                while i+1 < len(word) and char == word[i+1]:
                    i += 1
                    counter += 1
                newStr.append((char, counter))
                i += 1 # Move to next
            return newStr
        
        cS = compressWord(S)   # Compressed S
        ans = 0
        
        for w in words:
            nW = compressWord(w)
            if len(nW) != len(cS):
                continue
            for i in range(len(nW)):
                nChar, nCount = nW[i]
                sChar, sCount = cS[i]
                if nChar != sChar or nCount > sCount:   # Check if chars are not equal, or word has more char than streched words.
                    break
                if sCount < 3 and nCount != sCount:   # if less than 3 and count not equal
                    break
            else:
                ans += 1
        return ans

                
    # Four pointer solution to check two strings
    def check(S, W):
        i, j, i2, j2, n, m = 0, 0, 0, 0, len(S), len(W)
        while i < n and j < m:
            if S[i] != W[j]: return False
            while i2 < n and S[i2] == S[i]: i2 += 1
            while j2 < m and W[j2] == W[j]: j2 += 1
            if i2 - i != j2 - j and i2 - i < max(3, j2 - j): return False
            i, j = i2, j2
        return i == n and j == m
                