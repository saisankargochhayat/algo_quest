class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


# The head of the list refers to the first node which contains the first item of the list.
# In turn, that node holds a reference to the next node (the next item) and so on.
# It is very important to note that the list class itself does not contain any node objects.
# Instead it contains a single reference to only the first node in the linked structure.

class UnorderedList:
    def __init__(self):
        self.head = None

    # check if list is empty
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)  # new node points to rest of list
        self.head = temp

    # linked list traversal
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current is None:
                print("No element present")
                return
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.remove(26)

mylist.printList()
