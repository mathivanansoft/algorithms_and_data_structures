# find median in a stream of numbers

import os
import sys

user_path = os.environ.get("USER_PATH")
sys.path.append(user_path)

from data_structures.min_heap import MinHeap
from data_structures.max_heap import MaxHeap

def find_median(min_hp, max_hp):
    if len(min_hp) == 0 and len(max_hp) == 0:
        raise Exception("No element found")

    if len(min_hp) == len(max_hp):
        print(min_hp.arr[0], max_hp.arr[0])
    elif len(min_hp) > len(max_hp):
        print(min_hp.arr[0])
    else:
        print(max_hp.arr[0])
        


if __name__ == "__main__":
    arr = [21, 3, 4, 5, 15, 22, 30, 40, 45, 50]
    min_hp = MinHeap()
    max_hp = MaxHeap()

    for elmnt in arr:
        if len(min_hp) == 0:
            min_hp.insert(elmnt)
        else:
            if min_hp.arr[0] < elmnt:
                min_hp.insert(elmnt)
            else:
                max_hp.insert(elmnt)

        if len(min_hp) - len(max_hp) > 1:
            data = min_hp.extract_min()
            max_hp.insert(data)

        if len(max_hp) - len(min_hp) > 1:
            data = max_hp.extract_max()
            min_hp.insert(data)
        find_median(min_hp, max_hp)
        