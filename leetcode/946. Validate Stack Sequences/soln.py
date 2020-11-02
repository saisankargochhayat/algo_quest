class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        i, j = 0, 0
        while i < len(pushed) and j < len(popped):
            # Lets start by pushing an element 
            st.append(pushed[i])
            
            # Now try popping as much as possible 
            while st and j < len(popped) and (st[-1] == popped[j]):
                st.pop()
                j += 1
            
            i += 1

        return True if j == len(popped) else False
