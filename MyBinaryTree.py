class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def _traverse(self):
    pass


def traverse(self):
    current_node = self.root
    left_node = current_node.left
    right_node = current_node.right
    if current_node is None:
        print("Empty Tree")
        return
    while left_node or right_node is not None:
        pass


def _print(self):
    print("  /\\\n /  \\\nx    y")


class BinaryTree:

    def __init__(self):
        self.root = None
        self.d = 0

    def _insert(self, node, key):
        new_node = TreeNode(key)
        if key < node.data:
            if node.left is None:
                node.left = new_node
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self._insert(node.right, key)

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _height(self, node):
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1

    def height(self):
        if self.root is None:
            return 0
        return self._height(self.root)

    def search(self,key):
        pass

bt = BinaryTree()
bt.insert(50)
bt.insert(30)
bt.insert(60)
bt.insert(70)
bt.insert(40)
bt.insert(80)
bt.insert(20)
bt.insert(55)
h = bt.height()
print(h)
