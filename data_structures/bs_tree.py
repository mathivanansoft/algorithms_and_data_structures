
from binary_tree import BinaryTree
from binary_node import Node


class BSTree(BinaryTree):
    
    def __init__(self):
        BinaryTree.__init__(self)

    def insert(self, data):
        self.root = self.__insert(self.root, data)

    def __insert(self, node, data):
        if node is None:
            return Node(data)
        if node.data > data:
            node.left = self.__insert(node.left, data)
        else:
            node.right = self.__insert(node.right, data)
        return node

    def delete(self, key):
        self.__delete(self.root, key)
            

    def __delete(self, node, key):
        if node is None:
            return

        if node.data > key:
            node.left = self.__delete(node.left, key)

        elif node.data < key:
            node.right = self.__delete(node.right, key)

        else:
            
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                in_order = self.__in_order_successor(node, node.data)
                node.data = in_order.data
                node.right = self.__delete(node.right, in_order.data)
        
        return node


    def in_order_successor(self, key):
        return self.__in_order_successor(self.root, key, None)

    def __in_order_successor(self, node, key, successor):
        if node is None:
            return None

        if node.data > key:
            return self.__in_order_successor(node.left, key, node)
        elif node.data < key:
            return self.__in_order_successor(node.right, key, successor)
        else:
            temp = self.find_min_val(node)
            if temp is None:
                return successor
            else:
                return temp

    def find_min_val(self, node):
        if node is None:
            return

        temp = node.right
        while temp and temp.left is not None:
            temp = temp.left
        return temp

    def in_order_predecessor(self, key):
        return self.__in_order_predecessor(self.root, key, self.root)

    def __in_order_predecessor(self, node, key, predecessor):
        if node is None:
            return None

        if node.data > key:
            return self.__in_order_predecessor(node.left, key, predecessor)
        elif node.data < key:
            return self.__in_order_predecessor(node.right, key, node)
        else:
            temp = self.find_max_val(node)
            if temp is None:
                return predecessor
            else:
                return temp

    def find_max_val(self, node):
        if node is None:
            return

        temp = node.left
        while temp and temp.right is not None:
            temp = temp.right
        return temp


if __name__ == "__main__":
    b = BSTree()
    b.insert(25)
    b.insert(15)
    b.insert(10)
    b.insert(5)
    b.insert(18)
    b.insert(19)
    b.insert(20)
    b.insert(40)
    b.insert(45)
    b.insert(49)
    b.insert(44)
    b.insert(35)

        
