class MergeSort:
    def __init__(self,a):
        self.a = a

    def result(self):
        self.partialSort(0,len(self.a)-1)
        return self.a
    def partialSort(self,left,right):
        if left == right:
            return
        mid = int((left+right)/2)
        self.partialSort(left,mid)
        self.partialSort(mid+1,right)
        tempArray = []
        ptr1 = left
        ptr2 = mid+1
        for i in range(right-left+1):
            if self.a[ptr1] < self.a[ptr2]:
                tempArray.append(self.a[ptr1])
                ptr1 += 1
                if ptr1 > mid:
                    break
            else:
                tempArray.append(self.a[ptr2])
                ptr2 += 1
                if ptr2 > right:
                    break
        while(ptr1 <= mid):
            tempArray.append(self.a[ptr1])
            ptr1 += 1
        while(ptr2 <= right):
            tempArray.append(self.a[ptr2])
            ptr2 += 1
        k = 0
        for i in range(left,right+1):
            self.a[i] = tempArray[k]
            k += 1
