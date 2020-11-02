class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nCounter, hCounter = 0, 0
        while hCounter < len(haystack) and nCounter < len(needle):
            if needle[nCounter] == haystack[hCounter]:
                nCounter += 1
            else:
                hCounter -= nCounter # move back that many elements and start from the next element to it.
                nCounter = 0 # Reset needle counter           
            hCounter += 1
        if nCounter == len(needle):
            return hCounter - nCounter
        return -1
    
    # Zip and take substring and match
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for n, h in zip(needle, haystack[i:]):
                if n != h:
                    break
            else:
                return i
        return -1
        
    # Always faster to use a for loop! 
    def strStr(self, haystack: str, needle: str) -> int: 
        if not haystack and not needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(0, len(needle)):
                if needle[j] != haystack[i+j]:
                    break
            else:
                return i
        return -1