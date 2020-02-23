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