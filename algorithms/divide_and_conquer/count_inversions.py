# find the number of elements are inverted
# arr[1] > arr[2] means inverted


tot = 0
def count_inversions(arr):
    global tot
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    count_inversions(left)
    count_inversions(right)
    tot += merge (arr, left, right)
    return tot

def merge(arr, left, right):
    l = len(left)
    r = len(right)
    a = len(arr)
    i,j = 0,0
    pos = 0
    count = 0
    while i< l and j < r:
        if left[i] > right[j]:
            arr[pos] = right[j]
            j +=1
            count += l -i
        else:
            arr[pos] = left[i]
            i +=1
        pos +=1

    while i< l:
        arr[pos] = left[i]
        i +=1
        pos +=1
    while j<r:
        arr[pos] = right[j]
        j +=1
        pos +=1
    return count

if __name__ == "__main__":
    tot = 0
    arr = [7, 5, 1, 3, 4, 6]
    print("Count", count_inversions(arr))