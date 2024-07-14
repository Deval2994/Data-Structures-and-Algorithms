from MyLinkedList import Node


class Stack:

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        newNode = Node(value)

        newNode.next = self.top
        self.top = newNode

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

    def traverse(self):
        if self.isEmpty():
            return "Empty Stack"
        current = self.top
        while current is not None:
            print(current.data, end=" ")
            current = current.next
