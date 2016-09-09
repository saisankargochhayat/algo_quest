#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monks-love-for-food/
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    def peek(self):
        return self.items.peek()
        
def main():
    n=int(input())
    s=Stack()
    for i in range(n):
        #input values in the same line
        ch=list(map(int, input().split()))
        if ch[0]==1:
            if s.is_empty():
                print("No Food")
            else :
                print(s.pop())
        if ch[0]==2:
            s.push(ch[1])
        #clears the list and replace with a empty list
        del ch[:]
main()
