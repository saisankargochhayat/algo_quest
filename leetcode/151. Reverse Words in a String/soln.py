class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(' ')
        newwords = []
        [newwords.append(word) if len(word) > 0 else None for word in words]
        return ' '.join(newwords[::-1])
