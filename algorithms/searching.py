def linear_search(arr, key):
	for index, elmnt in enumerate(arr):
		if key == elmnt:
			return index
	return -1

def binary_search(arr, start, end, key):
	if start <= end:
		mid = start + (end - start + 1) // 2
		if arr[mid] == key:
			return mid
		elif key < arr[mid]:
			return binary_search(arr, start, mid-1, key)
		else :
			return binary_search(arr, mid+1, end, key)
	else:
		return -1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(binary_search(arr, 0, len(arr)-1, 6))