from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = defaultdict(int)
        frq = {}
        for i in nums:
            numsDict[i] += 1
        print(numsDict)
        
        for z,v in numsDict.items():
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        # We iterate from Length of Nums to 0 to check in frq and return result. 
        arr = []
        for x in range(len(nums), 0, -1):
            if x in frq:                
                for i in frq[x]:
                    arr.append(i)

        return arr[:k]
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = defaultdict(int)
        for i in nums:
            numsDict[i] += 1
        sortedDict = sorted(numsDict.items(), key=lambda x: x[1], reverse=True)
        # print(sortedDict)
        result = [sortedDict[i][0] for i in range(k)]
        return result
