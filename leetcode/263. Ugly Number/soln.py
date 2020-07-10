class Solution:
    def isUgly(self, num: int) -> bool:
        multiples = [30, 15, 6, 5, 3, 2]
        for x in multiples:
            while x <= num and num % x == 0:
                num /= x
        return True if num == 1 else False
