class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        countDic = Counter(nums)
        resSet = set()
        for key in countDic.keys():
            if k == 0 and countDic[key] > 1:
                resSet.add((key, key+k))
            elif k > 0:
                if key+k in countDic:
                    resSet.add((key, key+k))
                if key-k in countDic:
                    resSet.add((key-k, key))
        return len(resSet)
