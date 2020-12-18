class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        numOfZeros = arr.count(0)
        i, j, n = len(arr)-1, len(arr)-1, len(arr)
        while (i > -1) and numOfZeros:
            # print(i, j, numOfZeros, arr)
            if i + numOfZeros < n:
                    arr[i + numOfZeros] = arr[i]
                    j -= 1
            if arr[i]  == 0:
                numOfZeros -= 1   # Crucial to notice here, we subtract first as that zero is removed and then sum is done. 
                if i + numOfZeros < n:
                    arr[i + numOfZeros] = arr[i]
            i -= 1  # process next character
            

# class Solution(object):
#     def duplicateZeros(self, arr):
#         n = len(arr)
#         cntZero = arr.count(0)
#         newLen = n + cntZero # Length of new array if we don't trim up to length `n`
        
#         # Let's copy values from the end
#         i = n - 1
#         j = newLen - 1
#         while i >= 0:
#             if j < n: arr[j] = arr[i]
#             j -= 1
#             if arr[i] == 0: # Copy twice if arr[i] == 0
#                 if j < n: 
#                     arr[j] = arr[i]
#                 j -= 1
#             i -= 1
