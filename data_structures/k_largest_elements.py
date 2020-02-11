import os
import sys

user_path = os.environ.get("USER_PATH")
sys.path.append(user_path)

from data_structures.min_heap import MinHeap

def k_largest_elements(arr, k):
    temp = []
    heap = MinHeap(temp)

    for elmnt in arr:
        if len(heap) < k:
            heap.insert(elmnt)
        else:
            if elmnt > temp[0]:
                heap.extract_min()
                heap.insert(elmnt)

    output = []
    for _ in range(0, k):
        output.append(heap.extract_min())
    output.reverse()

    return output

if __name__ == "__main__":
    arr = [10,20,30,50,100,15]
    k = 3
    output = k_largest_elements(arr, k)
    print(output)