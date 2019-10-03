class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        common = [res.append(list(set(a))[0]) for a in itertools.takewhile(lambda x: len(set(x)) == 1, [x for x in zip(*strs)])]
        return "".join(res)
     
        
     # Enumeration soln
     # def longestCommonPrefix(self, strs):
     #    """
     #    :type strs: List[str]
     #    :rtype: str
     #    """
     #    if not strs:
     #        return ""
     #    shortest = min(strs,key=len)
     #    for i, ch in enumerate(shortest):
     #        for other in strs:
     #            if other[i] != ch:
     #                return shortest[:i]
     #    return shortest 

