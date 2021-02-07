from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastPos, seen, currMax = {}, set(), -1
        res = []
        for i in range(0, 26):
            c = chr(97+i)
            lastPos[c] = S.rfind(c)
        for i, c in enumerate(S):
            # Encounter new index higher than currMax
            if i > currMax:
                res.append(currMax+1)
            currMax = max(currMax, lastPos[c])
        res.append(len(S))
        ans = [res[i]-res[i-1] for i in range(1, len(res))]
        return ans