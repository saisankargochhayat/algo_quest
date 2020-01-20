class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        "A string having a k times repeating substring should the same string if k characters are rotated."
        for i in range(1,len(s)//2+1):
            if s == s[i:]+s[:i]:
                return True
            
# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         l = len(s)
#         counter = 1
#         while counter <= l/2:
#             substring = s[:counter]
#             if s.count(substring) == l/counter:
#                 return True
#             counter+=1
#         return False 
        
        
