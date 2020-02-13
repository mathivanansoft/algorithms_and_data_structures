
# find the majority element in a sorted arr which occurs more than n/2 times

def find_majority_element(arr):
    end = len(arr)
    mid = end // 2

    if end & 1 is 0:
        mid -= 1

    for index in range(0, mid+1):
        if arr[index] == arr[index+mid]:
            return True
    return False
        

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 4]
    print(find_majority_element(arr))
    arr = [1, 1, 1, 2]
    print(find_majority_element(arr))
    arr = [1, 2, 2]
    print(find_majority_element(arr))