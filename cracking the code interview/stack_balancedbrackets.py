#https://www.hackerrank.com/challenges/ctci-balanced-brackets
#http://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
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
        return self.items[-1]
    def size(self):
        return len(self.items)
def is_matched(expression):
    s=Stack()
    for x in expression:
        if x=='{' or x=='[' or x=='(':
            s.push(x)
        if x=='}' or x==']' or x==')':
            if s.is_empty():
                return False
            elif x == '}' and s.peek()=='{':
                s.pop()
            elif x == ')' and s.peek()=='(':
                s.pop()
            elif x == ']' and s.peek()=='[':
                s.pop()
            else:
                return False
    if s.is_empty():
        return True
t=int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
