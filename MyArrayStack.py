class ArrStack:

    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = 0

    def push(self, value):
        if self.top == self.size:
            print("stack overflow")
        else:
            self.stack[self.top] = value
            self.top += 1

    def pop(self):
        if self.top == 0:
            print("Empty stack")
        else:
            self.top -= 1

    def traverse(self):

        for i in range(self.top-1, -1, -1):
            print(self.stack[i], end="\n")


s = ArrStack(3)
s.push(7)
s.push(5)
s.push(6)
s.pop()
print(s.stack)
s.traverse()
