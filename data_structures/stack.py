class Stack(list):
    def __init__(self, size):
        list.__init__(self, [])
        self.size = size

    def push(self, data):
        if self.size > len(self):
            self.append(data)
        else:
            raise Exception("Stack overflow")

    def pop(self):
        if len(self) != 0:
            return list.pop(self)
        else:
            raise Exception("Stack underflow")

    def __repr__(self):
        return "{0} {1}".format(self.size, list(self).__str__())


if __name__ == "__main__":
    s = Stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print("After pushed", s)
    s.pop()
    print("After popped", s)