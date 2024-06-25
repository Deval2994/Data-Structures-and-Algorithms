from MyList import MyList

l = MyList()
l.append("hello")
l.append("44.4")
l.append(154)
l.append(False)
l.append("dev")
l.append(456)

print(l)
l.insert(1, 56)
print(l)
del l[1]
print(l)

l.remove("w")
print(l)

from MyLinkedList import LinkedList

ll = LinkedList()

ll.insert_node(1)
ll.insert_node(2)
ll.insert_node(3)

ll.insert_node(4)
ll.append(7)
ll.append(9)
ll.append(8)
ll.append(6)
print(ll.traverse())
print(ll[0])
# del l[2]
del ll[0]
# del l[4]
print(ll.traverse())


from MyStack import Stack
s = Stack()
# s.push(5)
# s.push(3)
# s.push(6)
print("Stack \n")
print(s.traverse())
print(s.peek())
s.pop()
print(s.traverse())