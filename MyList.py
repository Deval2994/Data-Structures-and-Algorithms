import ctypes


class MyList:

    def __init__(self):
        self.size = 1  # maximum capacity of array
        self.n = 0  # number of item present in array
        self.A = self.__createArray(self.size)

    def __len__(self):  # length of array (no of items)
        return self.n

    def append(self, item):
        if self.size == self.n:
            self.__resize(self.size)  # resize

        self.A[self.n] = item  # append and increase the maximum capacity
        self.n += 1

    def pop(self):
        if self.n == 0 :
            return "Empty List"
        self.n -= 1

    def clear(self):
        self.n = 0
        self.size = 1

    def __resize(self, capacity):
        newCapacity = capacity * 2  # double the capacity
        b = self.__createArray(newCapacity)  # create new array
        for i in range(self.n):  # Copy the item of original array to new array
            b[i] = self.A[i]

        self.A = b
        self.size = newCapacity

    def __str__(self):
        result = ''
        for i in range(self.n):
            result += f"{self.A[i]}, "
        return "[" + result[:-2] + "]"

    def __getitem__(self, item):
        return self.A[item] if 0 <= item < self.n else "Invalid Index - Index Out Of Bound"

    def find(self, target):
        for i in range(self.n):
            if self.A[i] == target:
                return i

        return "Item not found"

    def insert(self,index, item):
        if self.size == self.n:
            self.__resize(self.size)  # resize

        for i in range(self.n, index, -1):
            self.A[i] = self.A[i-1]

        self.A[index] = item
        self.n += 1

    def __delitem__(self, index):
        if index >= self.n:
            return "index out if bound"
        for i in range(index,self.n - 1):
            self.A[i] = self.A[i+1]
        self.n -= 1

    def remove(self, target):
        index = self.find(target)
        self.__delitem__(index) if type(index) == int else None

    def __createArray(self, capacity):
        return (capacity * ctypes.py_object)()

