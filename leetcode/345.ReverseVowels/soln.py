class Solution:
    # Two pointer approach
    def reverseVowels(self, s: str) -> str:
        sList = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        start, end = 0, len(s)-1
        while start < end:
            if sList[start] in vowels and sList[end] in vowels:
                sList[end], sList[start] = sList[start], sList[end]
                start, end = start+1, end-1
            # if left is vowel, and right is not
            elif sList[start] in vowels:
                end -= 1
            # right is vowel
            elif sList[end] in vowels:
                start += 1
            else:
                start, end = start+1, end-1
        return "".join(sList)
    
    # List approach
#     def reverseVowels(self, s: str) -> str:
#         sList = list(s)
#         vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#         mem, L = [], len(sList)
        
#         for i in range(L):
#             if sList[i] in vowels:
#                 mem.append(sList[i])
#                 sList[i] = None
#         vowelL = len(mem)
#         for j in range(L):        
#             if sList[j] is None:
#                 sList[j] = mem[vowelL-1]
#                 vowelL -= 1
#         return "".join(sList)
    