# A Python program to demonstrate common binary heap operations
# Import the heap functions from python library
from heapq import heappush,heapop,heapify
class Minheap:
    #Constructor to initialize a heap
    def __init__(self):
        self.heap=[]
    def parent(self,i):
        return (i-1)/2

    #Insert a new key "k"
    def insertKey(self,k)
        heappush(self.heap,k)
    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self,i,new_val):
        self.heap=new_val
