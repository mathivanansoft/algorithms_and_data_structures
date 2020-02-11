class MinHeap(object):
    def __init__(self, arr=[]):
        self.arr = arr

    def build_heap(self):
        l = len(self.arr)
        end = l // 2 - 1
        for index in range(end, -1, -1):
            self.heapify(index)

    def heapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2

        mininum = index
        if left < len(self.arr) and self.arr[index] > self.arr[left]:
            mininum = left
        if right < len(self.arr) and self.arr[mininum] > self.arr[right]:
            mininum = right
        if mininum != index:
            temp = self.arr[mininum]
            self.arr[mininum] = self.arr[index]
            self.arr[index] = temp
            self.heapify(mininum)

    def extract_min(self):
        if not len(self.arr):
            raise Exception("HEAP is empty")
        else:
            minimum = self.arr[0]
            self.arr[0] = self.arr[-1]
            self.arr.pop()
            self.heapify(0)
            return minimum

    def insert(self, elmnt):
        self.arr.append(elmnt)
        l = len(self.arr) - 1
        parent = l // 2
        if (l & 1) != 1:
            parent -= 1

        while parent >= 0:
            if self.arr[parent] > self.arr[l]:
                temp = self.arr[parent]
                self.arr[parent] = self.arr[l]
                self.arr[l] = temp
                l = parent
                if (parent & 1) != 1:
                    parent = parent // 2
                    parent -= 1
                else:
                    parent = parent // 2
            else:
                break

    def __len__(self):
        return len(self.arr)

    def __repr__(self):
        return str(self.arr)

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    print("MIN HEAP", arr)
    obj = MinHeap(arr)
    obj.build_heap()
    # extract min is similar to delete min.
    print("AFTER MIN HEAP: ", obj)
    minimum = obj.extract_min()
    print("EXTRACTED element", minimum)
    print("AFTER EXTRACTION", obj)
    minimum = obj.extract_min()
    print("EXTRACTED element", minimum)
    print("AFTER EXTRACTION", obj)
    minimum = obj.extract_min()
    print("EXTRACTED element", minimum)
    print("AFTER EXTRACTION", obj)
    minimum = obj.extract_min()
    print("EXTRACTED element", minimum)
    print("AFTER EXTRACTION", obj)
    minimum = obj.extract_min()
    print("EXTRACTED element", minimum)
    print("AFTER EXTRACTION", obj)