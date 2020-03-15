import os, sys

user_path = os.environ.get("USER_PATH")
sys.path.append(user_path)

from data_structures.bs_tree import BSTree
from data_structures.binary_node import Node as BNode

class Node(BNode):
    def __init__(self, data):
        BNode.__init__(self, data)
        self.height = 0


class AVL(BSTree):
    def __init__(self):
        BSTree.__init__(self)

    def insert(self, data):
        self.root = self.__insert(self.root, data)

    def __insert(self, node, data):
        if node is None:
            return Node(data)

        if node.data > data:
            node.left = self.__insert(node.left, data)

        else:
            node.right = self.__insert(node.right, data)

        node.height = self.height(node)
        bal = self.get_balance_factor(node)

        if bal > 1 and node.left.data > data:
            # right rotate
            grand_parent = node
            parent = grand_parent.left

            grand_parent.left = parent.right
            parent.right = grand_parent
            # height
            grand_parent.height = self.height(grand_parent)
            parent.height = self.height(parent)
            return parent

        elif bal > 1 and node.left.data < data:
            # left right rotate
            grand_parent = node
            parent = grand_parent.left
            child = parent.right

            grand_parent.left = child
            c1 = child.left
            child.left = parent
            parent.right = c1
            parent.height = self.height(parent)
            parent = child

            grand_parent.left = parent.right
            parent.right = grand_parent
            # height
            grand_parent.height = self.height(grand_parent)
            parent.height = self.height(parent)
            return parent
        
        elif bal < -1 and node.right.data < data:
            # left rotate
            grand_parent = node
            parent = grand_parent.right

            grand_parent.right = parent.left
            parent.left = grand_parent
            
            # height
            grand_parent.height = self.height(grand_parent)
            parent.height = self.height(parent)
            return parent

        elif bal < -1 and node.right.data > data:
            # right left rotate
            grand_parent = node
            parent = grand_parent.right
            child = parent.left

            grand_parent.right = child
            temp = child.right
            child.right = parent
            parent.left = temp
            parent.height = self.height(parent)
            parent = child

            grand_parent.right = parent.left
            parent.left = grand_parent

            # height
            grand_parent.height = self.height(grand_parent)
            parent.height = self.height(parent)

            return parent

        return node

    def get_balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
        