
# find the minimum cost to merge the patterns

import os
import sys

user_path = os.environ.get("USER_PATH")
sys.path.append(user_path)

from data_structures.min_heap import MinHeap


def optimal_merge(heap):
    min_cost = 0
    while len(heap):
        min_first = heap.extract_min()
        if len(heap):
            min_second = heap.extract_min()
            min_cost += min_first
            min_cost += min_second
        else:
            break
        heap.insert(min_first + min_second)

    return min_cost
    
    
if __name__ == "__main__":
    patterns = [10,20,30]
    heap = MinHeap(patterns)
    heap.build_heap()
    min_cost = optimal_merge(heap)
    print("MIN COST", min_cost)