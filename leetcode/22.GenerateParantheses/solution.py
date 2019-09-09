class Solution:
    def genPar(self, openB, closeB, n, result, soln):
        #Base case
        if (closeB == n):
            soln.append(''.join(result))
        else:
            if (closeB < openB):
                result.append(")")
                Solution.genPar(self, openB, closeB+1, n, result, soln)
                result.pop()
            if (openB < n):
                result.append("(")
                Solution.genPar(self, openB+1, closeB, n, result, soln)
                result.pop()
            
    def generateParenthesis(self, n: int) -> List[str]:
        soln = []
        Solution.genPar(self, 0, 0, n, [], soln)
        return soln
    