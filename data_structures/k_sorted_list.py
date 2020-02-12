# In a k sorted lists, find the minimum range in which
# atleast one element belongs to every list

import os
import sys

user_path = os.environ.get("USER_PATH")
sys.path.append(user_path)

from data_structures.min_heap import MinHeap

class K_Ordered(object):
    def __init__(self, data, kind, next_index):
        self.data = data
        self.kind = kind
        self.next_index = next_index

    def __eq__(self, other):
        return self.data == other.data

    def __ge__(self, other):
        return self.data >= other.data

    def __le__(self, other):
        return self.data <= other.data

    def __gt__(self, other):
        return self.data > other.data

    def __ne__(self, other):
        return self.data != other.data

    def __lt__(self, other):
        return self.data < other.data

    def __repr__(self):
        return "{}".format(self.data)
        
def find_minimum_range(source):
    k = len(source)
    arr = []
    maximum = K_Ordered(0, -1, -1)
    minimum = float("inf")
    range_ = float("inf")
    start, end = minimum, maximum

    for index in range(0, len(source)):
        elmnt = source[index]
        obj = K_Ordered(elmnt[0], index, 1)
        arr.append(obj)

        if obj > maximum:
            maximum = obj

    heap = MinHeap(arr)
    heap.build_heap()

    while True:
        minimum = heap.extract_min()
        if range_ > (maximum.data - minimum.data + 1):
            range_ = (maximum.data - minimum.data + 1)
            start = minimum.data
            end = maximum.data
            
        if minimum.next_index < len(source[minimum.kind]):
            elmnt = source[minimum.kind][minimum.next_index]
            temp = K_Ordered(elmnt, minimum.kind, minimum.next_index+1)
            heap.insert(temp)

            if temp > maximum:
                maximum = temp
        else:
            break

    return start, end, range_

        

if __name__ == "__main__":
    arr = [15, 27, 35, 42]
    arr1 = [12, 14, 16, 21]
    arr2 = [10, 25, 55, 67]
    arr3 = [23, 33, 41, 43]
    t = [arr, arr1, arr2, arr3]
    start, end, range_ = find_minimum_range(t)
    print("Start: ", start , "End: ", end, "Range", range_)