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


l = LinkedList()

l.insert_node(1)
l.insert_node(2)
l.insert_node(3)
l.insert_node(4)
l.insert_node(5)
print()
