class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        z = -1
        for i, num in enumerate(A):
            if num > z:
                z = i   # First positive num found
                break
        l,r = z - 1, z   # Left pointer == neg
        if z == -1:  
            return [i**2 for i in A[::-1]]    # if no positive found
        
        res = []
        while l >= 0 and r < len(A):
            if A[l]**2 < A[r]**2:
                res.append(A[l]**2)
                l -= 1
            else:
                res.append(A[r]**2)
                r += 1
        while l > -1:  # Remaining negative elements
            res.append(A[l]**2)
            l -= 1
        while r < len(A):  # Remaining pos elements
            res.append(A[r]**2)
            r += 1
        return res
            
        
            
            
