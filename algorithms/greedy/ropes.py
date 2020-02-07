
# n ropes with different length
# tie into single rope with minimum cost

import os
import sys

user_path = os.environ.get("USER_PATH")
sys.path.append(user_path)

from data_structures import min_heap as heap


def find_min_cost(ropes):
    min_cost = 0
    while len(ropes):
        min_first = heap.extract_min(ropes)
        if len(ropes):
            min_second = heap.extract_min(ropes)
        else:
            min_cost = min_first
            break
        heap.insert(ropes, min_first + min_second)

    return min_cost
    
    
if __name__ == "__main__":
    ropes = [2,3,5,7,9,13]
    heap.build_min_heap(ropes)
    min_cost = find_min_cost(ropes)
    print("MIN COST", min_cost)