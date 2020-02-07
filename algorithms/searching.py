def linear_search(arr, key):
	for elmnt in arr:
		if key == elmnt:
			return True
	return False

def binary_search(arr, start, end, key):
	if start <= end:
		mid = start + (end - start + 1)/2
		if arr[mid] == key:
			return True
		elif key < arr[mid]:
			return binary_search(arr, start, mid-1, key)
		else :
			return binary_search(arr, mid+1, end, key)
	else:
		return False
