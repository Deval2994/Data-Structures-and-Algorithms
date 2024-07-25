class LP_Dictionary:  # Linear probing

    def __init__(self, size):
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)

        if self.slot[hash_value] is None:
            self.slot[hash_value] = key
            self.data[hash_value] = value

        else:

            if self.slot[hash_value] == key:
                self.data[hash_value] = value

            else:

                while self.slot[hash_value] is not None and self.slot[hash_value] != key:
                    hash_value = self.rehash(hash_value)

                self.slot[hash_value] = key
                self.data[hash_value] = value

    def __setitem__(self, key, value):
        self.put(key, value)

    def hash_function(self, key):
        return abs(hash(key)) % self.size

    def rehash(self, prev_hash):
        return (prev_hash + 1) % self.size

    def get(self, key):
        hash_value = self.has_function(key)
        current_hash = hash_value
        while self.slot[current_hash] is not None:
            if self.slot[current_hash] == key:
                return self.data[current_hash]

            current_hash = self.rehash(current_hash)

            if current_hash == hash_value:
                return "item not found"

        return "item not found"

    def traverse(self):
        result = "[ "
        for i in range(len(self.slot)):
            if self.slot[i] is not None:
                result += f"{self.slot[i]} : {self.data[i]},\n  "
        print(result[:-4], "]")


from MyList import MyList


class Node:

    def __init__(self, key, value):
        self.key = key
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

    def insert_node(self, key, value):  # link 2
        newNode = Node(key, value)

        newNode.next = self.head

        self.head = newNode
        self.n += 1

    def traverse(self):  # Need modification
        current = self.head

        result = ''

        while current is not None:
            result += f" {current.key} : {current.data} ->"
            current = current.next

        print(f"--> {result[1:-3]}")

    def remove(self, item):
        if self.head == None:
            return print("List is empty")
        current = self.head
        if current.data == item:
            self.head = self.head.next
            return

        while current.next.data != item:
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


class Chain_Dictionary:

    def __init__(self, size):
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size
        self.n = 0
        self.bucket = self.make_array(size)

    def make_array(self, capacity):
        l = MyList()

        for i in range(capacity):
            l.append(LinkedList())

        return l

    def put(self, key, value):
        bucket_index = self.hash_function(key)

        ll = self.bucket[bucket_index]

        current = self.found_key(key)

        if current is None:
            ll.insert_node(key, value)

        elif current == -1:
            new_node = Node(key, value)
            current = ll.head
            while current.next is not None:
                current = current.next

            current.next = new_node
            self.n += 1

        else:
            current.data = value


    def hash_function(self, key):
        return abs(hash(key)) % self.size

    def rehash(self, prev_hash):
        return (prev_hash + 1) % self.size

    def get(self, key):
        current = self.found_key(key)

        if current is not None and current != -1:
            return current.data

    def found_key(self, key):
        bucket_index = self.hash_function(key)
        ll = self.bucket[bucket_index]
        current = ll.head
        if current is None:
            return None

        if current.key == key:
            return current

        while current.next is not None:
            if current.key == key:
                return current
            current = current.next

        return -1

    def traverse(self):
        for bucket_index in range(self.size):
            if self.bucket[bucket_index].head is not None:
                self.bucket[bucket_index].traverse()


