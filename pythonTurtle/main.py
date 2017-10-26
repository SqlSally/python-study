class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        n = Node(data)
        if self.isEmpty():
            self.head = n
        else:
            n.next = self.head
            self.head = n
        self.size += 1

    def delete(self):
        if not self.isEmpty():
            self.head = self.head.next
            self.size -= 1

    def print(self):
        x = self.head
        while x is not None:
            print(x)
            x = x.next

    def isEmpty(self):
        return self.size == 0
