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

    def traverse(self):
        current = self.head

        result = ''

        while current is not None:
            result += f" {current.data} ->"
            current = current.next

        return result[1:-3]

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

    def remove(self,value):
        if self.head == None:
            return print("List is empty")
        current = self.head
        while current.next.data != value:
            current = current.next

        memory = current.next.next
        current.next = memory
        self.n -= 1

l = LinkedList()

l.insert_node(1)
l.insert_node(2)
l.insert_node(3)

l.insert_node(4)
l.append(7)
l.append(9)
l.append(8)
l.append(6)

print(l.traverse())
l.append_after(2, 20)

print(l.traverse())

l.delete_tail()
print(l.traverse())

l.remove(7)
print(l.traverse())