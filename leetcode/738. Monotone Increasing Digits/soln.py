class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        num_str = str(N)
        num_list = [int(s) for s in num_str]
        r = len(num_list)-1
        l = r-1
        while l >= 0:
            # if its decreasing
            if num_list[l] > num_list[r]:
                # We reduce left by 1 and convert everything to right to 9. 
                num_list[l] -= 1
                # Set everything right of this to 9, being greedyyy
                for i in range(r, len(num_list)):
                    num_list[i] = 9
            l -= 1
            r -= 1
        
        res = ""
        for i in range(len(num_list)):
            if num_list[i] != 0:
                break
        num_list = num_list[i:]
        
        
        return "".join([str(i) for i in num_list])
