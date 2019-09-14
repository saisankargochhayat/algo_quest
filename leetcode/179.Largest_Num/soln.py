
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:    
    def largestNumber(self, nums):
        array = sorted(map(str, nums), key=LargerNumKey)
        # print(array)
        largest_num = "".join(array)
        return '0' if largest_num[0] == '0' else largest_num
