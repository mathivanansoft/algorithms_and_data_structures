from bs_tree import BSTree

class Node(object):

    def __init__(self, data):
        self.data = data
        self.color = "R"
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.data == other.data

    def __gt__(self, other):
        return self.data > other.data

    def __lt__(self, other):
        return self.data < other.data

    def __ge__(self, other):
        return self.data >= other.data

    def __le__(self, other):
        return self.data <= other.data

    def __ne__(self, other):
        return self.data != other.data
        
    def __repr__(self):
        return "{0} {1}".format(self.data, self.color)

class RedBlackTree(BSTree):

    def __init__(self):
        BSTree.__init__(self)

    def insert(self, data):
        self.root = self.__insert(self.root, data)
        if self.root.color == "R":
            self.root.color = "B"


    def __insert(self, node, data):

        if node is None:
            return Node(data)

        if node.data > data:
            node.left = self.__insert(node.left, data)
            grand_parent = node
            parent = node.left
            sibling = node.right

            if parent.left or parent.right:
                # Parent and Sibling is Red
                if sibling and parent.color == "R" and sibling.color == "R":
                    parent.color = "B"
                    sibling.color = "B"
                    grand_parent.color = "R"
                    return grand_parent
                # Parent is Red and Sibling is Black or None
                elif parent.color == "R":
                    if parent.left and parent.left.color == "R":
                        # right rotate
                        par_right_child = parent.right
                        parent.right = grand_parent
                        grand_parent.left = par_right_child
                        grand_parent.color = "R"
                        parent.color = "B"
                        return parent
                    elif parent.right and parent.right.color == "R":
                        # left rotate
                        par_right_child = parent.right
                        grand_parent.left = par_right_child
                        temp = par_right_child.left
                        par_right_child.left = parent
                        parent.right = temp
                        
                        # right rotate
                        parent = par_right_child
                        par_right_child = parent.right
                        parent.right = grand_parent
                        grand_parent.left = par_right_child
                        grand_parent.color = "R"
                        parent.color = "B"
                        return parent
                        
                return grand_parent

        else:
            node.right = self.__insert(node.right, data)
            grand_parent = node
            parent = node.right
            sibling = node.left

            if parent.left or parent.right:
                # Parent and Sibling is Red
                if sibling and parent.color == "R" and sibling.color == "R":
                    # case 2
                    parent.color = "B"
                    sibling.color = "B"
                    grand_parent.color = "R"
                    return grand_parent
                # Parent is Red and Sibling is Black or None
                elif parent.color == "R":
                    if parent.right and parent.right.color == "R":
                        # left rotate
                        par_left_child = parent.left
                        parent.left = grand_parent
                        grand_parent.right = par_left_child
                        grand_parent.color = "R"
                        parent.color = "B"
                        return parent

                    elif parent.left and parent.left.color == "R":
                        # right rotate
                        par_left_child = parent.left
                        grand_parent.right = par_left_child
                        temp = par_left_child.right
                        par_left_child.right = parent
                        parent.left = temp

                        # left rotate
                        parent = par_left_child
                        par_left_child = parent.left
                        parent.left = grand_parent
                        grand_parent.right = par_left_child
                        grand_parent.color = "R"
                        parent.color = "B"
                        return parent

        return node            

    def delete(self, key):
        self.__delete(self.root, key)
        if self.root is not None:
            if self.root.color == "R" or self.root.color == "BB":
                self.root.color = "B"
            

    def __delete(self, node, key):
        if node is None:
            return

        if node.data > key:
            node.left = self.__delete(node.left, key)

        elif node.data < key:
            node.right = self.__delete(node.right, key)

        else:
            
            if node.left is None and node.right is None:
                if node.color == "R":
                    return None
                elif node.color == "B":
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


if __name__ == "__main__":
    r = RedBlackTree()
    # r.insert(5)
    # r.insert(3)
    # r.insert(7)
    # r.insert(1)
    # r.insert(4)
    # r.insert(9)
    # r.insert(6)
    # r.insert(10)
    
    # r.insert(11)
    # r.insert(3)
    # r.insert(14)
    # r.insert(15)
    # r.insert(1)
    # r.insert(7)
    # r.insert(-1)
    # r.insert(2)
    # r.insert(5)
    # r.insert(8)
    
    # insertion
    b = RedBlackTree()
    b.insert(23)
    b.insert(5)
    b.insert(30)
    b.insert(14)
    b.insert(17)
    b.insert(40)
    b.insert(45)
    b.insert(27)
    b.insert(29)
    b.insert(26)
    b.pre_order_traversal()
    
    r = RedBlackTree()
    r.insert(10)
    r.insert(8)
    r.insert(11)
        