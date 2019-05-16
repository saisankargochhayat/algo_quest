#https://www.hackerrank.com/challenges/ctci-find-the-running-median
from heapq import *
class Spliter:
    def __init__(self):
        #minheap
        self.upper = []
        #max heap
        self.lower = []
        
    def median(self):
        #for odd length arrays
        if len(self.upper) > len(self.lower):
            return self.upper[0]
        #for even length arrays 
        else:
            return (self.upper[0] - self.lower[0]) / 2.
    def print(self):
        for i in range(len(self.upper)):
            print(heappop(self.upper)) 
    def add(self, value):
        value = heappushpop(self.upper, value)
        print("value is at upper ",value)
        value = -heappushpop(self.lower, -value)
        print("value is at lowerr ",value)
        print(self.upper,self.lower)
        if len(self.upper) <= len(self.lower):
            heappush(self.upper, value)
        else:
            heappush(self.lower, -value)

s = Spliter()
n = int(input())
for i in range(n):
    m = int(input())
    s.add(m)
    print("at main func",s.upper,s.lower)
    print(s.median()/1.0)
