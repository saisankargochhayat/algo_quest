# Binary search solution O(log n)
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        low, high = 0, len(A)-1
        while low <= high:
            mid = low + (high-low)//2
            # Check mid
            if A[mid-1] < A[mid] > A[mid+1]:
                return mid
            elif A[mid] < A[mid+1]:
                low = mid + 1
            else:
                high = mid - 1

# O(N/2)
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i, j = 0, len(A)-1
        while i <= j:
            if A[i] > A[i+1]:
                return i
            elif A[j-1] < A[j]:
                return j
            i += 1
            j -= 1
        