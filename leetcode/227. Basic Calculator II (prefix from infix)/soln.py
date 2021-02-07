# Idea is maintain current number and when you encounter next operation, calculate past operation and append to stack. 
# Sum the stack in the end and return result. 
class Solution:
    def calculate(self, s: str) -> int:
        operation = '+'
        s += operation
        st, currNum = [], ""
        operators = {'+','-','*','/'}
        for c in s:
            if c.isdigit():
                currNum += c
            elif c in operators:  # Encountering sum operators
                currNum = int(currNum)
                if operation == '-':
                    st.append(-currNum)
                elif operation == '*':
                    temp = st.pop()
                    st.append(temp * currNum)
                elif operation == '/':
                    temp = st.pop()
                    if temp < 0:
                        st.append(-1*(-1*temp // currNum))
                    else:
                        st.append(temp // currNum)
                else:
                    st.append(currNum)
                operation = c
                currNum = ""
        ans = sum(st)
        return ans