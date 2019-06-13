# Problem link - https://leetcode.com/problems/kth-largest-element-in-an-array/
class Heap:
    def __init__(self,A):
        self.A = A
        self.heapSize = len(self.A)
    # This method maintains the max heap property.
    def max_heapify(self, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2
        if left < self.heapSize and self.A[left] >= self.A[largest]:
            largest = left
        else: largest = i
        if right < self.heapSize and self.A[right] >= self.A[largest]:
            largest = right
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]        
            self.max_heapify(largest)
    
    # We can use the procedure  MAX-HEAPIFYin a bottom-up manner to convert  anarrayAŒ1 : : n,wherenDA:length,  into  a  max-heap.
    # The procedure BUILD-MAX-HEAPgoes throughthe remaining nodes of the tree and runs MAX-HEAPIFYon each one.
    def build_max_heap(self):
        for i in range(int((self.heapSize/2)),-1,-1):
            self.max_heapify(i)
    
    def extract_max(self):
        if self.heapSize < 1:
            return None
        maximum = self.A[0]
        self.A[0] = self.A[self.heapSize-1]
        self.heapSize -= 1
        self.max_heapify(0)
        return maximum
    
    def heap_sort(self):
        self.build_max_heap()
        for i in range(self.heapSize-1,0,-1):
            self.A[0], self.A[i] = self.A[i], self.A[0]
            self.heapSize -= 1
            self.max_heapify(0)
        return self.A

# Testing heap sort!
myHeap = Heap([1,2,3,-17,4,7,9,12,8])
print(myHeap.heap_sort())

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        myHeap = Heap(nums)
        myHeap.build_max_heap()
        maximum = None
        while k != 0:
            maximum = myHeap.extract_max()
            k -= 1
        return maximum