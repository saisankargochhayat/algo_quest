class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        level = -1
        result = 0
        
        # We iterate through the sorted list.
        for i in sorted(A):
            # If the level is less than num, we do nothing, it means A[i-1] < A[i]
            if level < i:
                level = i
            # We just increase the level by 1, and add the difference to the result.
            else:
                level += 1
                result += level - i
        return result
    
