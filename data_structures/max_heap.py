class MaxHeap(object):
    def __init__(self, arr=[]):
        self.arr = arr

    def build_heap(self):
        children = len(self.arr) // 2
        for index in range(children, -1, -1):
            self.heapify(index)
    
    def heapify(self, index):
        length = len(self.arr)
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < length and self.arr[index] < self.arr[left]:
            largest = left
        else:
            largest = index

        if right < length and self.arr[largest] < self.arr[right]:
            largest = right
        
        if largest != index:
            temp = self.arr[largest]
            arr[largest] = self.arr[index]
            self.arr[index] = temp
            self.heapify(largest)


    def extract_max(self):
        if not len(self.arr):
            raise Exception("HEAP is empty")
        else:
            maximum = self.arr[0]
            self.arr[0] = self.arr[-1]
            self.arr.pop()
            self.heapify(0)
            return maximum

    def insert(self, elmnt):
        self.arr.append(elmnt)
        l = len(self.arr) - 1
        parent = l // 2
        if (l & 1) != 1:
            parent -= 1

        while parent >= 0:
            if self.arr[l] > self.arr[parent]:
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
    arr = [1, 2, 3, 4, 5]
    obj = MaxHeap(arr)
    obj.build_heap()
    # extract max is similar to delete max.
    print("AFTER MAX HEAP: ", obj)
    maxi = obj.extract_max()
    print("EXTRACTED element", maxi)
    print("AFTER EXTRACTION", obj)
    maxi = obj.extract_max()
    print("EXTRACTED element", maxi)
    print("AFTER EXTRACTION", obj)
    maxi = obj.extract_max()
    print("EXTRACTED element", maxi)
    print("AFTER EXTRACTION", obj)
    maxi = obj.extract_max()
    print("EXTRACTED element", maxi)
    print("AFTER EXTRACTION", obj)
    maxi = obj.extract_max()
    print("EXTRACTED element", maxi)
    print("AFTER EXTRACTION", obj)

    