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

        while current.next != None:
            current = current.next

        newNode = Node(value)
        current.next = newNode
        self.n += 1



l = LinkedList()
l.insert_node(44)
l.append(7)
l.append(9)
l.append(8)
l.append(6)
print(l.traverse())
