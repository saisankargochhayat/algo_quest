class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict) # Converted to set for O(1)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        mem = defaultdict(list)
        
        def _wordBreak_topdown(s):
            """ return list of word lists """
            # Because word is empty
            if not s:
                return [[]]  # list of empty list
            # return cached solution
            if s in mem:
                return mem[s]
            
            # Start top-down hunt
            for endIndex in range(1, len(s)+1):
                # Prefix word (all prefix words)
                word = s[:endIndex]
                if word in wordSet:
                    # Like subsentence would be ("cat" + _wordBreak_topdown("sanddog")
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        mem[s].append([word] + subsentence)
            
            return mem[s]
        
        # break the input string into lists of words list
        _wordBreak_topdown(s)
        # print(mem)
        # chain up the lists of words into sentences.
        return [" ".join(words) for words in mem[s]]
