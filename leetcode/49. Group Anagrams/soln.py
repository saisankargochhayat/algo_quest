# Just hash the words into counts of char and tuple them. O(NK)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

# O(NKlogK) because we are sorting K
# from collections import defaultdict
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         result_dic, res = defaultdict(list), []
#         for word in strs:
#             keyStr = "".join(sorted(word))
#             result_dic[keyStr].append(word)
#         return result_dic.values()
