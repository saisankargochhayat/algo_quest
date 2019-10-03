# This can also be solved by using an two pointer approach skipping the not isalum() characters. 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newString = []
        for i in s:
            if i.isalnum():
                newString.append(i)
        newStr = "".join(newString)
        # print(newStr, newStr[::-1])
        return newStr == newStr[::-1]
        