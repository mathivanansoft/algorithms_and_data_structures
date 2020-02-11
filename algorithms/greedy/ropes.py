
# n ropes with different length
# tie into single rope with minimum cost

import os
import sys

user_path = os.environ.get("USER_PATH")
sys.path.append(user_path)

from data_structures.min_heap import MinHeap


def find_min_cost(heap):
    min_cost = 0
    while len(heap):
        min_first = heap.extract_min()
        if len(heap):
            min_second = heap.extract_min()
        else:
            min_cost = min_first
            break
        heap.insert(min_first + min_second)

    return min_cost
    
    
if __name__ == "__main__":
    ropes = [2,3,5,7,9,13]
    heap = MinHeap(ropes)
    heap.build_heap()
    min_cost = find_min_cost(heap)
    print("MIN COST", min_cost)