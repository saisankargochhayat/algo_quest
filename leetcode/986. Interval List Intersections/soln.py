## Idea is we take one element from a and b serially and take increase pointer based on,
## And bump up the counter if a range cannot be found out with that pair. 
from typing import List
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # Here 
        a, b = 0, 0
        res = []
        l_A, l_B = len(A), len(B)
        while a < l_A and b < l_B:
            a_x, a_y = A[a]
            b_x, b_y = B[b]
            
            if a_y < b_x:
                a += 1
            elif b_y < a_x:
                b += 1
            else:
                interval = [max(a_x, b_x), min(a_y, b_y)]
                res.append(interval)
                if a_y < b_y:
                    a += 1
                elif b_y < a_y:
                    b += 1
                else:
                    a,b = a+1, b+1
        print(res)



    


soln = Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])

soln = Solution().intervalIntersection([[0,100]], [[1,5],[8,12],[15,24],[25,26]])