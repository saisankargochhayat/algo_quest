from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = Counter(A[0])
        for word in A:
            res &= Counter(word) # Intersection of counters
        return list(res.elements())  # elements() return duplicates which keys doesn't, ignoring 0. 


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        allWords, res = [], []
        for word in A:
            allWords.append(Counter(word))
        for c in A[0]:
            for w in allWords:
                if c not in w.keys():
                    break
                if w.get(c) <= 0:
                    break
                w[c] -= 1
            else:
                res.append(c)  
        return res
