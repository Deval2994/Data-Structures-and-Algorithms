from MyLinkedList import Node


class MyQueue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.rear = new_node
            self.front = self.rear
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Empty Queue")
        else:
            self.front = self.front.next

    def  front_item(self):
        if self.front is not None:
            return self.front.data

    def  rear_item(self):
        if self.front is not None:
            return self.rear.data

    def isEmpty(self):
        return self.front is None

    def traverse(self):
        if self.front is None:
            print("Empty Queue")
        else:
            current = self.front
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()
