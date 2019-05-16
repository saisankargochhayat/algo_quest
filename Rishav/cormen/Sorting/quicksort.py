class QuickSort:
    def __init__(self,a):
        self.a = a
         
    def result(self):
        self.partialSort(0,len(self.a)-1)
        return self.a

    def partialSort(self,left,right):
        if left == right or right < left:
            return
        index = self.partition(left,right)
        self.partialSort(left,index-1)
        self.partialSort(index+1,right)

    def partition(self,left,right):
        pivot = self.a[right]
        i = left - 1
        for j in range(left,right):
            if self.a[j] < pivot:
                i += 1
                self.a[j],self.a[i] = self.a[i],self.a[j]
        self.a[i+1],self.a[right] = self.a[right],self.a[i+1]
        return i+1
