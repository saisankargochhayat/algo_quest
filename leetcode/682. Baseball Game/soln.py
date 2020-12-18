class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = 0
        st = []
        for op in ops:
            if op == '+':
                temp = st[-1] + st[-2]
                res += temp
                st.append(temp)              
            elif op == "C":
                res -= st[-1]
                st.pop()
            elif op == "D":
                temp = st[-1] * 2
                res += temp
                st.append(temp)
            else:
                st.append(int(op))
                res += int(op)
        return res
                
                
