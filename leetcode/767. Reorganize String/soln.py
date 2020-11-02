class Solution:
    def reorganizeString(self, S: str) -> str:
        from collections import Counter
        res = []
        sMap = Counter(S)  # we have a map of char to count
        cArr = [[k, sMap[k]] for k in sMap.keys()]  # max length 26
        if not len(cArr):
            return ""
        while len(cArr) >= 2:
            cArr.sort(key=lambda x: x[1], reverse=True)
            if cArr[1][1] >= 1:
                cArr[0][1] -= 1    # if both top two characters have values
                cArr[1][1] -= 1
                res.extend([cArr[0][0], cArr[1][0]])
            elif cArr[0][1] >= 1:
                res.append(cArr[0][0])  # if only character has values
                cArr[0][1] -= 1
                break
            else:
                break   # if no one has values. 
        # Final element
        if cArr[0][1] > 0:
            return ""   # remaining characters in top value
        return "".join(res)
        
        
