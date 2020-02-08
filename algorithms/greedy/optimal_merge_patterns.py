
# find the minimum cost to merge the patterns

import os
import sys

user_path = os.environ.get("USER_PATH")
sys.path.append(user_path)

from data_structures import min_heap as heap


def optimal_merge(patterns):
    min_cost = 0
    while len(patterns):
        min_first = heap.extract_min(patterns)
        if len(patterns):
            min_second = heap.extract_min(patterns)
            min_cost += min_first
            min_cost += min_second
        else:
            break
        heap.insert(patterns, min_first + min_second)

    return min_cost
    
    
if __name__ == "__main__":
    patterns = [10,20,30]
    heap.build_min_heap(patterns)
    min_cost = optimal_merge(patterns)
    print("MIN COST", min_cost)