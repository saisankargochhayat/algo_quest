class Solution:
    def isPalindrome(self, x: int) -> bool:
        X = x
        if x<0 or (x%10 == 0 and x!=0):
            return False
        reverse = 0
        while x > reverse:
            m = x%10
            x = x//10
            reverse = 10*reverse+m
        # print(x, reverse)
        return reverse == x or reverse//10 == x
