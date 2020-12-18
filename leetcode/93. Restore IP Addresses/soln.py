class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:   
            return []
        
        def backtrack(i, curr, k):
            # Base condition
            if k == 0:
                if i == len(s):
                    curr.pop() # remove last dot 1.1.1.1. -> 1.1.1.1
                    res.append("".join(curr))
                return
            if i > len(s)-1:
                return
            # Scenario 1 put dot after 1 element
            curr.extend([s[i],'.'])
            backtrack(i+1, curr[:], k-1)
            del curr[-2:]
            # Scenario 2 put dot after 2 digits
            if i + 1 < len(s) and s[i] != '0':
                twoDigits = s[i]+s[i+1]
                curr.extend([twoDigits,'.'])
                backtrack(i+2, curr[:], k-1)
                del curr[-2:]
            # Put dot after 3 digits
            if i + 2 < len(s) and s[i] != '0':
                threeDigits = twoDigits + s[i+2]
                if int(threeDigits) <= 255:
                    curr.extend([threeDigits,'.'])
                    backtrack(i+3, curr[:], k-1)
                    del curr[-2:]
        
        res = []
        backtrack(0, [], 4)
        return res
