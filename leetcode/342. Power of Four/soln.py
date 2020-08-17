# Math solution
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        from math import log2
        return num > 0 and log2(num) % 2 == 0

# Basic solution
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num % 4 == 0 and num >= 1:
            num /= 4
        if num == 1:
            return True
        return False
        
	
