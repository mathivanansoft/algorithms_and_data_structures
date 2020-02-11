class Stack(object):
    def __init__(self, size):
        self.size = size
        self.arr = []

    def push(self, data):
        if self.size > len(self.arr):
            self.arr.append(data)
        else:
            raise Exception("Stack overflow")

    def pop(self):
        if len(self.arr) != 0:
            return self.arr.pop()
        else:
            raise Exception("Stack underflow")

if __name__ == "__main__":
    s = Stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print("After pushed", s.arr)
    s.pop()
    print("After popped", s.arr)