class Queue(object):
    def __init__(self, size):
        self.size = size
        self.arr = []

    def enqueue(self, data):
        if self.size > len(self.arr):
            self.arr.append(data)
        else:
            raise Exception("Queue overflow")

    def dequeue(self):
        if len(self.arr) != 0:
            return self.arr.pop(0)
        else:
            raise Exception("Queue underflow")



if __name__ == "__main__":
    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("After Enqueue", q.arr)
    q.dequeue()
    print("After Dequeue", q.arr)