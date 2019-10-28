class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        closingBraces =[ ')', '}', ']']
        openingBraces = ['(', '{', '[']
        
        st = list(s)
        temp = []
        
        while st:
            curr = st.pop()
            if curr in closingBraces:
                temp.append(curr)
            elif len(temp) == 0:
                return False
            else:
                temp2 = temp.pop()
                if curr == '(':
                    if temp2 == ')':
                        pass
                    else:
                        return False
                elif curr == '{':
                    if temp2 == '}':
                        pass
                    else:
                        return False
                elif curr == '[':
                    if temp2 == ']':
                        pass
                    else:
                        return False
        if len(temp) == 0:
            return True
        else:
            return False
