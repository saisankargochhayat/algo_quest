# Clear prefix product array on incoming 0
class ProductOfNumbers:
    def __init__(self):
        self.A = [1]

    def add(self, a):
        if a == 0:
            self.A = [1]
        else:
            self.A.append(self.A[-1] * a)

    def getProduct(self, k):
        if k >= len(self.A): return 0
        return self.A[-1] // self.A[-k - 1]



class ProductOfNumbers:

    def __init__(self):
        self.l = 0
        self.p = []  # Prefix multiplication
        self.zPos = None  # Latest pos of zero

    def add(self, num: int) -> None:
        self.l += 1
        # We encoutner zero 
        if num == 0:
            self.zPos = self.l
        if self.p:
            pNum = self.p[-1]*num if self.p[-1] != 0 else num  # next prod 
            self.p.append(pNum)  # append prod to prefux mul arr
        else:
            self.p.append(num)

            

    def getProduct(self, k: int) -> int:
        if self.zPos and self.zPos > self.l-k:
            return 0   #If zero is included in product 
        divBy = self.p[self.l-k-1] if self.p[self.l-k-1] > 0 and self.l-k-1 >= 0 else 1
        return self.p[-1] // divBy
            


# Naive Solution
class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.l = 0

    def add(self, num: int) -> None:
        self.arr.append(num)
        self.l += 1

    def getProduct(self, k: int) -> int:
        subArr = self.arr[self.l-k:]
        res = 1
        for i in subArr:
            res = res * i
        return res


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
