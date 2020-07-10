class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = bin(x)[2:], bin(y)[2:]
        res = 0
        shorter = x if len(x) <= len(y) else y
        longer = y if len(y) >= len(x) else x
        shorter = ('0' * abs(len(x) - len(y))) + shorter
        # print(shorter, longer)
        for i in range(len(longer)):
            if shorter[i] != longer[i]:
                res += 1
        return res