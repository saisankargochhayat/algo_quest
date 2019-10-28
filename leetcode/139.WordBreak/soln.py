class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Converting the given word dict to set to ensure O(1) average case access. 
        wordDictSet = set(wordDict)
        l = len(s)
        # Lets have a boolean array that has if the substring till 'i' can be broken into pieces that is contained by word dict. 
        dp = [False]*(len(s)+1)
        dp[0] = True
        # Here dp[] contains if the letter i in the word till that point holds true according to the quesiton. 
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and (s[j:i] in wordDictSet):
                    #print(s[j:i])
                    dp[i] = True
                    break
        #print(dp)
        return dp[l]
