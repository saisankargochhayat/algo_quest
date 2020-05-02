class Solution:
    def intToRoman(self, num: int) -> str:
        romanDict = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
        l = len(romanDict)-1
        n = num
        res = ""
        while n > 0 and l > -1:
            number, roman = romanDict[l]
            if n >= number:
                quotient = n//number
                res = res + str(quotient*roman)
                n = n%number
            l -= 1
        
        return res
        
