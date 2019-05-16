class BubbleSort:
    def __init__(self,a):
        self.a = a
    def result(self):
        for i in range(len(self.a)):
            for j in range(i+1,len(self.a)):
                if self.a[i] > self.a[j]:
                    self.a[i],self.a[j] = self.a[j],self.a[i]
        return self.a
