class InsertionSort:
    def __init__(self,a):
        self.a = a

    def result(self):
        a = self.a
        for i in range(1,len(a)):
            for j in range(i-1,-1,-1):
                if a[j] > a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]
                else:
                    break
        return a
