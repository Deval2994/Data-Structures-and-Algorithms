class Node:

    def __init__(self, value):
        self.data = value
        self.next = None
        self.n = 0


class LinkedList:

    def __init__(self):
        # Empty Liked list
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_node(self, value):  # link 2
        newNode = Node(value)

        newNode.next = self.head

        self.head = newNode
        self.n += 1

    def __str__(self):
        current = self.head

        result = ''

        while current is not None:
            result += f" {current.data} ->"
            current = current.next

        return result[1:-3]

    def traverse(self):
        current = self.head

        result = ''

        while current is not None:
            result += f" {current.data} ->"
            current = current.next

        return print(result[1:-3])

    def append(self, value):

        if self.head == None:
            self.insert_node(value)
            return

        current = self.head

        while current.next is not None:
            current = current.next

        newNode = Node(value)
        current.next = newNode
        self.n += 1

    def append_after(self, after, value):
        if self.head == None:
            return print("List is empty")

        current = self.head

        newNode = Node(value)

        while current.next is not None:
            if current.data == after:
                break
            current = current.next

        if current.next == None:
            return print(f"No such element found : {after}")

        memory = current.next
        current.next = newNode
        current = current.next
        current.next = memory
        self.n = + 1

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return print("List is empty")
        self.head = self.head.next
        self.n -= 1

    def delete_tail(self):
        if self.head == None:
            return print("List is empty")
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.n -= 1

    def remove(self, value):
        if self.head == None:
            return print("List is empty")
        current = self.head
        if current.data == value:
            self.delete_head()
            return
        while current.next.data != value:
            current = current.next

        memory = current.next.next
        current.next = memory
        self.n -= 1

    def search(self, item):
        current = self.head
        position = 0
        while current.next is not None:
            if current.data == item:
                return position
            current = current.next
            position += 1
        return "Item not found"

    def __getitem__(self, item):
        current = self.head
        if item >= self.n:
            return "index out of bound"
        for i in range(item):
            current = current.next
        return current.data

    def __delitem__(self, key):

        self.remove(self.__getitem__(key))

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
