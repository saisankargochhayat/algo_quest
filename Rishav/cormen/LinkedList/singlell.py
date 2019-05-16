class Node:
    def __init__(self,payload = None,next = None):
        self.payload = payload
        self.next = next
    def __repr__(self):
            return repr(self.payload)
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) +']'

    def prepend(self,payload):
        self.head = Node(payload = payload, next = self.head)
    def append(self,payload):
        if not self.head:
            self.head = Node(payload = payload, next = None)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(payload = payload, next = None)
    def find(self, key):
        curr = self.head
        while curr and curr.payload != key:
            curr = curr.next
        return curr
    def remove(self,key):
        curr = self.head
        prev = None
        while curr and curr.payload != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr is not None:
            prev.next = curr.next
            curr.next = None
    def reverse(self):
        curr = self.head
        prev = None
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
