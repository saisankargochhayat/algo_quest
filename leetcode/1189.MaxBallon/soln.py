from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = collections.Counter(text)
        return min(c["b"], c["a"], c["l"] // 2, c["o"] // 2, c["n"])
    
    # def maxNumberOfBalloons(self, text: str) -> int:
    #     balloonDict = defaultdict(int)
    #     for i in text:
    #         if i in 'balloon':
    #             balloonDict[i] += 1
    #     counter = 0
    #     valuesExist = True
    #     balloonDict['l'] //= 2
    #     balloonDict['o'] //= 2
    #     result = []
    #     for i in 'balloon':
    #         result.append(balloonDict[i])
    #     return min(result)
