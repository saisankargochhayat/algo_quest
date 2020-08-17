# Stack solution, draw a graph, think accumulation from local minima to local maxima. 
class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        res = 1
        # Lets find the res for this element
        while self.stocks and self.stocks[-1][0] <= price:
            res += self.stocks.pop()[1]
        self.stocks.append((price, res))
        return res

# Naive Solution
# class StockSpanner:

#     def __init__(self):
#         self.stocks = [0]

#     def next(self, price: int) -> int:
#         self.stocks.append(price)
#         l = len(self.stocks)-1
#         curr = len(self.stocks)-2
#         for curr in range(curr, -1, -1):
#           if self.stocks[curr] > self.stocks[l]:
#                 return l - curr
#         return l


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
