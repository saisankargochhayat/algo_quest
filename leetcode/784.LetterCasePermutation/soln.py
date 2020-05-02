class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(sub = "", curr = 0):
            # Base case
            if len(sub) == l:
                res.append(sub)
            # Else we build up the solution with sub + letter(uppercase and lowercase)
            elif curr < l:
                if S[curr].isalpha():
                    backtrack(sub + S[curr].swapcase(), curr+1)
                backtrack(sub + S[curr], curr+1)
        res = []
        l = len(S)
        backtrack()
        return res
