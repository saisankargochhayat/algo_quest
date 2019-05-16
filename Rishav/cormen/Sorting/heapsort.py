class HeapSort:
    def __init__(self,a):
        self.a = a
        self.heapSize = len(self.a)
    def result(self):
        self.buildHeap()
        for i in range(len(self.a)-1,-1,-1):
            self.a[0],self.a[i] = self.a[i],self.a[0]
            self.heapSize -= 1
            self.heapify(0)
        return self.a

    def buildHeap(self):
        for i in range(int((len(self.a))/2),-1,-1):
            self.heapify(i)

    def heapify(self,i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2
        if left < self.heapSize and self.a[left] > self.a[largest]:
            largest = left
        if right < self.heapSize and self.a[right] > self.a[largest]:
            largest = right
        if not i == largest:
            self.a[i],self.a[largest] = self.a[largest],self.a[i]
            self.heapify(largest)
