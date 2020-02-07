
def insertion_sort(arr):
	
	for i in range(0, len(arr)):
		val = arr[i]
		while i>0 and val < arr[i-1]:
			arr [i] = arr[i-1]
			i = i-1
		arr[i] = val
	return arr

def bubble_sort(arr):
	end = len(arr)
	
	for i in range(0, len(arr)):
		for j in range(1, end):
			if arr[j-1] > arr[j]:
				temp = arr[j]
				arr[j] = arr[j-1]
				arr[j-1] = temp
		end = end-1
	return arr


def quick_sort(arr, start, end):
	if start < end:
		pindex = partition(arr, start, end)
		quick_sort(arr, start, pindex-1)
		quick_sort(arr, pindex+1, end)


def partition(arr, start, end):

	pivot = arr[end]
	pindex = start
	
	for i in range(start, end):
		if arr[i] < pivot:
			temp = arr[pindex]
			arr[pindex] = arr[i]
			arr[i] = temp
			pindex +=1

	temp = arr[pindex]
	arr[pindex] = arr[end]
	arr[end] = temp
	return pindex

def merge_sort(arr):
	if len(arr) < 2:
		return None
	mid = len(arr)/2
	left = arr[:mid]
	right = arr[mid:]
	merge_sort(left)
	merge_sort(right)
	merge(arr, left, right)

def merge(arr, left, right):
	l = len(left)
	r = len(right)
	a = len(arr)
	i,j = 0,0
	pos = 0
	while i< l and j < r:
		if left[i] > right[j]:
			arr[pos] = right[j]
			j +=1
		else:
			arr[pos] = left[i]
			i +=1
		pos +=1

	while i< l:
		arr[pos] = left[l]
		i +=1
		pos +=1
	while j<r:
		arr[pos] = right[j]
		i +=1
		pos +=1

if __name__ == '__main__':

	arr = [9,1,8,2,6,4,3,7,5]
	insertion_sort(arr)
	print ('insertion_sort', arr)


	arr1 = [9,1,8,2,6,4,3,7,5]
	bubble_sort(arr1)
	print ('bubble_sort', arr1)

	arr2 = [9,1,8,2,6,4,3,7,5]
	quick_sort(arr2, 0, 8)
	print ('quick_sort', arr2)

	arr3 = [9,1,8,2,6,4,3,7,5]
	quick_sort(arr3, 0, 8)
	print ('merge_sort', arr3)