from binary_node import Node

class BinaryTree(object):
    def __init__(self):
        self.root = None


    def pre_order_traversal(self):
        self.__pre_order_traversal(self.root)


    def __pre_order_traversal(self, node):
        if node is None:
            return None
        print(node)
        self.__pre_order_traversal(node.left)
        self.__pre_order_traversal(node.right)


    def in_order_traversal(self):
        self.__in_order_traversal(self.root)


    def __in_order_traversal(self, node):
        if node is None:
            return None
        self.__in_order_traversal(node.left)
        print(node)
        self.__in_order_traversal(node.right)


    def post_order_traversal(self):
        self.__post_order_traversal(self.root)


    def __post_order_traversal(self, node):
        if node is None:
            return None
        self.__post_order_traversal(node.left)
        self.__post_order_traversal(node.right)
        print(node)


    def level_order_traversal(self):
        if self.root is None:
            return

        arr = []
        arr.append(self.root)

        while len(arr):
            node = arr.pop(0)
            print(node)
            if node.left is not None:
                arr.append(node.left)
            if node.right is not None:
                arr.append(node.right)

    def size(self):
        return self.__size(self.root)

    def __size(self, node):
        if node is None:
            return 0

        left = self.__size(node.left)
        right = self.__size(node.right)
        return 1 + left + right

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
