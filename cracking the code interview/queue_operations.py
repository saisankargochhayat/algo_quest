#https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]

queue = Queue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.enqueue(values[1])
    elif values[0] == 2:
        queue.dequeue()
    else:
        print(queue.peek())
