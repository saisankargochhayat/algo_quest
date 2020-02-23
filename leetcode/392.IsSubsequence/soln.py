class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        start = 0
        for c in s:
            i = t.find(c, start)
            if i == -1:
                return False
            start = i + 1
        return True
        
        

# Simple Iterative Solution
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i = 0
#         j = 0
#         s_len, t_len = len(s), len(t)
        
#         while i<s_len and j<t_len:
#             if s[i] == t[j]:
#                 i+=1
#                 j+=1
#             else:
#                 j+=1
#         if i == s_len:
#             return True
#         else:
#             return False
