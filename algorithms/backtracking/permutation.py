

def permute(arr, start, end):
    # start, end is inclusive

    if start == end:
        print("".join(arr))

    else:
        for index in range(start, end+1):
            swap(arr, index, start)
            permute(arr, start + 1, end)
            swap(arr, index, start)


def swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp


if __name__ == "__main__":
    string = "ABCD"
    permute(list(string), 0, len(string)-1)
