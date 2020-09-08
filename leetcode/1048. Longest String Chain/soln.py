class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordSet = set(words[::-1])
        seen = {}
        res = 1
        for word in sorted(words, key=len):
            # we assume the chain of length to be 1. 
            seen[word] = 1
            
            for i in range(len(word)):
                prevWord = word[:i]+word[i+1:]
                if prevWord in seen:
                    seen[word] = max(seen[prevWord]+1, seen[word])
                    res = max(res, seen[word])
        return res
        
