from MyLinkedList import Node


class Stack:

    def __init__(self):
        self.top = None
        self.n = 0

    def __len__(self):
        return self.n

    def isEmpty(self):
        return self.n == 0

    def push(self, value):
        newNode = Node(value)

        newNode.next = self.top
        self.top = newNode
        self.n += 1

    def peek(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            return self.top.data

    def pop(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            self.top = self.top.next
            self.n -= 1

    def clear(self):
        self.top = None
        self.n = 0

    def traverse(self):
        if self.isEmpty():
            return "Empty Stack"
        current = self.top
        while current is not None:
            print(current.data)
            current = current.next

