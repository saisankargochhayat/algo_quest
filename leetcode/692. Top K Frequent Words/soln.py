# Implement comparator and use it in heap push. 
class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word
        
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        from heapq import heappush, heapreplace
        hp = []
        wordDic = Counter(words)
        for key in wordDic.keys():
            heappush(hp, Word(wordDic[key], key))
            if len(hp) > k:
                heappop(hp)
        
        res = [heappop(hp).word for _ in range(k)]
        return res[::-1]


# import collections
# import heapq
# import functools

# @functools.total_ordering
# class Element:
#     def __init__(self, count, word):
#         self.count = count
#         self.word = word
        
#     def __lt__(self, other):
#         if self.count == other.count:
#             return self.word > other.word
#         return self.count < other.count
    
#     def __eq__(self, other):
#         return self.count == other.count and self.word == other.word

# class Solution(object):
#     def topKFrequent(self, words, k):
#         """
#         :type words: List[str]
#         :type k: int
#         :rtype: List[str]
#         """
#         counts = collections.Counter(words)   
        
#         freqs = []
#         heapq.heapify(freqs)
#         for word, count in counts.items():
#             heapq.heappush(freqs, (Element(count, word), word))
#             if len(freqs) > k:
#                 heapq.heappop(freqs)
        
#         res = []
#         for _ in range(k):
#             res.append(heapq.heappop(freqs)[1])
#         return res[::-1]

Solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)