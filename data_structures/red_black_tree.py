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

    def __case3a(self, parent):
        # bb = double blackness
        # parent = bb's parent
        # sibling = bb's sibling

        # case 3
        # sibling is black and its children is either black or None
        # a) parent is red and sibling is right child of P

        bb = parent.left
        sibling = parent.right
        parent.color = "B"
        sibling.color = "R"
        bb.color = "B"
        if bb.data is None:
            parent.left = None
        return parent

    def __case3b(self, parent):
        # b) parent is red and sibling is left child of P

        bb = parent.right
        sibling = parent.left
        parent.color = "B"
        sibling.color = "R"
        bb.color = "B"
        if bb.data is None:
            parent.right = None
        return parent

    def __case3c(self, parent):
        # c) parent is black and sibling is right child of P

        bb = parent.left
        sibling = parent.right
        parent.color = "BB"
        sibling.color = "R"
        bb.color = "B"
        if bb.data is None:
            parent.left = None
        return parent

    def __case3d(self, parent):
        # d) parent is black and sibling is left child of P

        bb = parent.right
        sibling = parent.left
        parent.color = "BB"
        sibling.color = "R"
        bb.color = "B"
        if bb.data is None:
            parent.right = None
        return parent

    def __case4a(self, parent):
        # this case does n't remove double blackness
        # it switches to other case
        # sibling is red
        # a) sibling is right child of p

        bb = parent.left
        sibling = parent.right
        parent.color = "R"
        sibling.color = "B"

        parent.right = sibling.left
        sibling.left = self.__check_cases(sibling.left)
        return sibling

    def __case4b(self, parent):
        # b) sibling is left child of p

        bb = parent.right
        sibling = parent.left
        parent.color = "R"
        sibling.color = "B"

        parent.left = sibling.right
        sibling.right = parent
        sibling.right = self.__check_cases(sibling.right)

        return sibling

    def __case5a(self, parent):
        # sibling is black and sibling's right children is red
        # and sibling is right child of p

        bb = parent.left
        sibling = parent.right
        temp_color = parent.color
        parent.color = sibling.color
        sibling.color = temp_color
        sibling.right.color = "B"
        #left rotate
        parent.right = sibling.left
        sibling.left = parent

        if bb.data is None:
            parent.left = None
        else:
            parent.left.color = "B"

        return sibling

    def __case5b(self, parent):
        # sibling is black and sibling's left children is red
        # and sibling is left child of p

        bb = parent.right
        sibling = parent.left
        temp_color = parent.color
        parent.color = sibling.color
        sibling.color = temp_color
        sibling.left.color = "B"
        #right rotate

        parent.left = sibling.right
        sibling.right = parent

        if bb.data is None:
            parent.right = None
        else:
            parent.right.color = "B"

        return sibling

    def __case6a(self, parent):
        # sibling is black and sibling's right children is black
        # and sibling's left children is red
        # and sibling is right child of p

        bb = parent.left
        sibling = parent.right
        sl = sibling.left
        sr = sibling.right

        temp_color = sibling.color
        sibling.color = sl.color
        sl.color = temp_color

        sibling.left = sl.right
        sl.right = sibling
        return sl

    def __case6b(self, parent):
        # sibling is black and sibling's left children is black
        # and sibling's right children is red
        # and sibling is left child of p

        bb = parent.right
        sibling = parent.left
        sl = sibling.left
        sr = sibling.right

        temp_color = sibling.color
        sibling.color = sr.color
        sr.color = temp_color

        sibling.right = sr.left
        sr.left = sibling
        return sr

    def delete(self, key):
        self.root = self.__delete(self.root, key)
        if self.root is not None:
            if self.root.color == "R":
                self.root.color = "B"
            elif self.root.color == "BB":
                self.root.color = "B"
            if self.root.data is None:
                self.root = None

    def is_left_dd(self, parent):
        if parent.left is not None and parent.left.color == "BB":
            return True
        return False

    def is_right_dd(self, parent):
        if parent.right is not None and parent.right.color == "BB":
            return True
        return False

    def __delete(self, node, key):
        if node is None:
            return

        if node.data > key:
            node.left = self.__delete(node.left, key)

        elif node.data < key:
            node.right = self.__delete(node.right, key)

        else:
            if node.color == "R":
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    in_order = self.in_order_successor(node, node.data)
                    node.data = in_order.data
                    node.right = self.__delete(node.right, in_order.data)

            elif node.color == "B":
                if node.left is None and node.right is None:
                    node.color = "BB"
                    node.data = None
                    return node
                elif node.left is None and node.right.color == "R":
                    node.right.color = "B"
                    return node.right
                elif node.right is None and node.left.color == "R":
                    node.left.color = "B"
                    return node.left
                else:
                    in_order = self.in_order_successor(node, node.data)
                    node.data = in_order.data
                    node.right = self.__delete(node.right, in_order.data)

        return self.__check_cases(node)

    def __check_cases(self, parent):
        if self.is_left_dd(parent):
            sibling = parent.right

            if sibling.color == "B":
                sl = sibling.left
                sr = sibling.right

                if sr is not None and sr.color == "R":
                    return self.__case5a(parent)

                if ((sl is None and sr is None)
                    or ((sl is not None and sr is not None)
                    and (sl.color == "B" and sr.color == "B"))):
                    if parent.color == "R":
                        parent = self.__case3a(parent)
                    else:
                        parent = self.__case3c(parent)

                elif (sr is None or sr.color == "B") and sl.color == "R":
                    parent.right = self.__case6a(parent)
                    return self.__case5a(parent)
            else:
                sl = sibling.left
                sr = sibling.right
                return self.__case4a(parent)


        elif self.is_right_dd(parent):
            sibling = parent.left

            if sibling.color == "B":
                sl = sibling.left
                sr = sibling.right

                if sl is not None and sl.color == "R":
                    return self.__case5b(parent)

                if ((sl is None and sr is None)
                    or ((sl is not None and sr is not None)
                    and (sl.color == "B" and sr.color == "B"))):
                    if parent.color == "R":
                        parent = self.__case3b(parent)
                    else:
                        parent = self.__case3d(parent)

                elif (sl is None or sl.color == "B") and sr.color == "R":
                    parent.left = self.__case6b(parent)
                    return self.__case5b(parent)
            else:
                sl = sibling.left
                sr = sibling.right

                return self.__case4b(parent)

        return parent