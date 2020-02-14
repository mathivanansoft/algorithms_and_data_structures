# search an element in sorted rotated array

def search_in_sorted_rotated_arr(arr, key, start, end):
    if start > end:
        return -1
    else:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] < arr[end]:
            if key > arr[mid] and key <= arr[end]:
                return search_in_sorted_rotated_arr(arr, key, mid + 1, end)
            else:
                return search_in_sorted_rotated_arr(arr, key, start, mid - 1)
        else:
            if key >= arr[start] and key < arr[mid]:
                return search_in_sorted_rotated_arr(arr, key, start, mid - 1)
            else:
                return search_in_sorted_rotated_arr(arr, key, mid + 1, end)


if __name__ =="__main__":
    arr = [ 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
    print(search_in_sorted_rotated_arr(arr, 8, 0, len(arr)-1))
    