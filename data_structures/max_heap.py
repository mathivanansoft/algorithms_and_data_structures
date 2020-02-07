def max_heapify(arr, index, length):
    left = 2 * index + 1
    right = 2 * index + 2
    
    if left < length and arr[index] < arr[left]:
        largest = left
    else:
        largest = index
    
    if right < length and arr[largest] < arr[right]:
        largest = right
    
    if largest != index:
        temp = arr[largest]
        arr[largest] = arr[index]
        arr[index] = temp
        max_heapify(arr, largest, length)

def build_max_heap(arr):
    children = len(arr) // 2
    for index in range(children, -1, -1):
        max_heapify(arr, index, len(arr))

def extract_max(arr):
    if not len(arr):
        print("HEAP is empty")
    else:
        maximum = arr[0]
        arr[0] = arr[-1]
        arr.pop()
        max_heapify(arr, 0, len(arr))
        return maximum

def insert(arr, elmnt):
    arr.append(elmnt)
    l = len(arr) - 1
    parent = l // 2
    if (l & 1) != 1:
        parent -= 1

    while parent >= 0:
        if arr[l] > arr[parent]:
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
    arr = [1, 2, 3, 4, 5]
    build_max_heap(arr)
    # extract max is similar to delete max.
    print("AFTER MAX HEAP: ", arr)
    maxi = extract_max(arr)
    print("EXTRACTED element", maxi)
    print("AFTER EXTRACTION", arr)
    maxi = extract_max(arr)
    print("EXTRACTED element", maxi)
    print("AFTER EXTRACTION", arr)
    maxi = extract_max(arr)
    print("EXTRACTED element", maxi)
    print("AFTER EXTRACTION", arr)
    maxi = extract_max(arr)
    print("EXTRACTED element", maxi)
    print("AFTER EXTRACTION", arr)
    maxi = extract_max(arr)
    print("EXTRACTED element", maxi)
    print("AFTER EXTRACTION", arr)

    