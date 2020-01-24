class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # The stack initially has the base element. The first component of the tuple represents
        # and the second component is the count of that element.
        stack = [['*',0]]
        # Now for every char in the string. 
        for c in s:
            # Check with the previous tuple in the stack.
            if stack[-1][0] == c:
                stack[-1][1] += 1
                # if k characters already exist we start popping them.
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # If it doesnt matches we add this to the stack. 
                stack.append([c,1])
        # print(stack)
        res = ''.join(c*k for c,k in stack)
        return res
