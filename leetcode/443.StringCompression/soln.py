class Solution:
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0,0
        l = len(chars)
        # This runs to the end of the list.
        while fast<len(chars):
            # Replace with the next character.
            chars[slow] = chars[fast]
            counter = 1
            # we iterate till its same to the next character.
            while fast+1 < l and chars[fast] == chars[fast+1]:
                fast += 1
                counter += 1
            # now we replace first part of the array with the number of chars of the new char found if its more than 1.
            if counter > 1:
                for c in str(counter):
                    chars[slow+1] = c
                    slow += 1
            # Both move to the next point. 
            slow += 1
            fast += 1
        return slow
