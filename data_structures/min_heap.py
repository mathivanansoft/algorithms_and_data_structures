
def build_min_heap(arr):
    l = len(arr)
    end = l // 2 - 1
    for index in range(end, -1, -1):
        min_heapify(arr, index)

def min_heapify(arr, index):
    left = 2 * index + 1
    right = 2 * index + 2

    mininum = index
    if left < len(arr) and arr[index] > arr[left]:
        mininum = left
    if right < len(arr) and arr[mininum] > arr[right]:
        mininum = right
    if mininum != index:
        temp = arr[mininum]
        arr[mininum] = arr[index]
        arr[index] = temp
        min_heapify(arr, mininum)

def extract_min(arr):
    if not len(arr):
        print("HEAP is empty")
    else:
        minimum = arr[0]
        arr[0] = arr[-1]
        arr.pop()
        min_heapify(arr, 0)
        return minimum

def insert(arr, elmnt):
    arr.append(elmnt)
    l = len(arr) - 1
    parent = l // 2
    if (l & 1) != 1:
        parent -= 1

    while parent >= 0:
        if arr[parent] > arr[l]:
            temp = arr[parent]
            arr[parent] = arr[l]
            arr[l] = temp
            l = parent
            if (parent & 1) != 1:
                parent = parent // 2
                parent -= 1
            else:
                parent = parent // 2
        else:
            break


if __name__ == "__main__":
    arr = [5,4,3,2,1]
    print("MIN HEAP", arr)
    build_min_heap(arr)
    # extract min is similar to delete min.
    print("AFTER MIN HEAP: ", arr)
    minimum = extract_min(arr)
    print("EXTRACTED element", minimum)
    print("AFTER EXTRACTION", arr)
    minimum = extract_min(arr)
    print("EXTRACTED element", minimum)
    print("AFTER EXTRACTION", arr)
    minimum = extract_min(arr)
    print("EXTRACTED element", minimum)
    print("AFTER EXTRACTION", arr)
    minimum = extract_min(arr)
    print("EXTRACTED element", minimum)
    print("AFTER EXTRACTION", arr)
    minimum = extract_min(arr)
    print("EXTRACTED element", minimum)
    print("AFTER EXTRACTION", arr)
    
    
    